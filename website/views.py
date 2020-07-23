from .forms import StartupProjectFormNew, StartupProjectFormEdit, ApplicantForm
from .models import StartupProject, Employee, Applicant
from .utils import save_employees, request_is_correct, get_current_referrer, send_new_project_to_slack,\
    send_new_applicant_to_slack
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory, Textarea
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from itertools import chain
from operator import attrgetter
from sentry_sdk import capture_message


SAVED_HEADERS = {}


def home_page(request):
    """Отображает главную страницу"""
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render({}, request))


class AllCardsView(generic.ListView):
    """Отображает все карточки (проектов и соскателей)."""
    template_name = 'all_cards_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        startup_queryset = StartupProject.objects.all()
        applicant_queryset = Applicant.objects.all()
        return sorted(list(chain(startup_queryset, applicant_queryset)), key=attrgetter('upd_time'), reverse=True)


class ProjectView(generic.ListView):
    """Отображает карточки проектов."""
    template_name = 'projects_list.html'
    context_object_name = 'startups'

    def get_queryset(self):
        return StartupProject.objects.all().order_by('-upd_time')


class ApplicantView(generic.ListView):
    """Отображает карточки соискателей."""
    template_name = 'applicants_list.html'
    context_object_name = 'applicants'

    def get_queryset(self):
        return Applicant.objects.all().order_by('-upd_time')


def new_applicant(request):
    """Отображает форму соискателя или сохраняет её."""
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save()
            link = request.build_absolute_uri(reverse('applicants_list'))
            send_new_applicant_to_slack(applicant, link)
        return HttpResponseRedirect(reverse('applicants_list'))
    form = ApplicantForm()
    template = loader.get_template('new_applicant.html')
    return HttpResponse(template.render({'form': form}, request))


def new_project(request, project_type):
    """
    Отображает форму для добавления нового проекта или сохраняет её.
    Отправляет сообщение о добавлении нового проекта в slack.
    """
    template = loader.get_template('new_project.html')
    if request.method == 'POST':
        form = StartupProjectFormNew(request.POST)
        if form.is_valid():
            startup = form.save(commit=False)
            startup.project_type = project_type
            startup.save()
            employees_list = save_employees(startup, form)
            link = request.build_absolute_uri(reverse('projects_list'))
            send_new_project_to_slack(startup, employees_list, link)
        return HttpResponseRedirect(reverse('projects_list'))
    else:
        form = StartupProjectFormNew()
        return HttpResponse(template.render({'form': form, 'project_type': project_type}, request))


def edit_project(request, startup_id):
    """Отображает форму для редактирования карточки проекта или сохраняет изменения.
    В случае попытки доступа по прямому запросу отображает 403."""
    if request_is_correct(request):
        with open('request_is_correct_urls.txt', 'a') as file:
            print(request.META.get('HTTP_REFERER'), file=file)
        template = loader.get_template('edit_project.html')
        startup = StartupProject.objects.get(id=startup_id)
        EmployeeFormSet = inlineformset_factory(
            StartupProject,
            Employee,
            fields=('employee',),
            extra=1,
            widgets={'employee': Textarea(attrs={'class': 'form-control', 'rows': 6})}
        )
        if request.method == "POST":
            form = StartupProjectFormEdit(request.POST, instance=startup)
            formset = EmployeeFormSet(request.POST, instance=startup)
            if form.is_valid() and formset.is_valid():
                form.save()
                formset.save()
            return HttpResponseRedirect(reverse(SAVED_HEADERS.get('HTTP_REFERER', 'projects_list')))
        form = StartupProjectFormEdit(instance=startup)
        formset = EmployeeFormSet(instance=startup)
        return HttpResponse(template.render({'form': form, 'formset': formset, 'startup_id': startup_id}, request))
    else:
        raise PermissionDenied


def edit_applicant(request, applicant_id):
    """Отображает форму для редактирования анкеты соискателя или сохраняет изменения.
    В случае попытки доступа по прямому запросу отображает 403."""
    if request_is_correct(request):
        with open('request_is_correct_urls.txt', 'a') as file:
            print(request.META.get('HTTP_REFERER'), file=file)
        template = loader.get_template('edit_applicant.html')
        applicant = Applicant.objects.get(id=applicant_id)
        if request.method == "POST":
            form = ApplicantForm(request.POST, instance=applicant)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse(SAVED_HEADERS.get('HTTP_REFERER', 'projects_list')))
        form = ApplicantForm(instance=applicant)
        return HttpResponse(template.render({'form': form, 'applicant_id': applicant_id}, request))
    else:
        raise PermissionDenied


def delete_project(request, startup_id):
    """Удаляет карточку проекта или отображает 403 при попытке доступа по прямой ссылке."""
    if request_is_correct(request):
        with open('request_is_correct_urls.txt', 'a') as file:
            print(request.META.get('HTTP_REFERER'), file=file)
        StartupProject.objects.get(id=startup_id).delete()
        return HttpResponseRedirect(reverse(SAVED_HEADERS.get('HTTP_REFERER', 'projects_list')))
    else:
        raise PermissionDenied


def delete_applicant(request, applicant_id):
    """Удаляет карточку соискателя или отображает 403 при попытке доступа по прямой ссылке."""
    if request_is_correct(request):
        with open('request_is_correct_urls.txt', 'a') as file:
            print(request.META.get('HTTP_REFERER'), file=file)
        Applicant.objects.get(id=applicant_id).delete()
        return HttpResponseRedirect(reverse(SAVED_HEADERS.get('HTTP_REFERER', 'applicants_list')))
    else:
        raise PermissionDenied


def project_access_check(request, startup_id):
    """Проверяет доступ к карточке проекта по паролю. В случае успеха переводит на страницу
    редактирования проекта, при неудаче, возращает на исходную с сообщением об ошибке."""
    startup = StartupProject.objects.get(id=startup_id)
    if request.method == 'POST':
        if request.POST['password'] == startup.password:
            SAVED_HEADERS['HTTP_REFERER'] = get_current_referrer(request)
            return HttpResponseRedirect(reverse('edit_project', args=(startup_id,)))
        messages.warning(request, 'Неверный пароль')
        return HttpResponseRedirect(reverse('projects_list'))


def applicant_access_check(request, applicant_id):
    """Проверяет доступ к анкете соискателя по паролю. В случае успеха переводит на страницу
    редактирования анкеты, при неудаче, возращает на исходную с сообщением об ошибке."""
    applicant = Applicant.objects.get(id=applicant_id)
    if request.method == 'POST':
        if request.POST['password'] == applicant.password:
            SAVED_HEADERS['HTTP_REFERER'] = get_current_referrer(request)
            return HttpResponseRedirect(reverse('edit_applicant', args=(applicant_id,)))
        messages.warning(request, 'Неверный пароль')
        return HttpResponseRedirect(reverse('applicants_list'))


def sentry_check(request):
    a = 1 / 0


def not_found(request, exception=None):
    capture_message("Page not found", level='error')
    template = loader.get_template('404_not_found.html')
    return HttpResponse(template.render({'message': 'Такой страницы нет'}, request), status=404)


def permission_denied(request, exception=None):
    capture_message("Permission denied", level='error')
    template = loader.get_template('403_forbidden.html')
    return HttpResponse(template.render({'message': 'Так не работает'}, request), status=403)
