from django import forms
from .models import StartupProject, Applicant


class StartupProjectFormNew(forms.ModelForm):
    """
    Форма для создания новой карточки проекта.
    Содержит все поля модели StartupProject и три
    дополнительных поля для сотрудников.
    """
    employee1 = forms.CharField(label='Хотим в команду',
                                widget=forms.Textarea)
    employee2 = forms.CharField(label='Хотим в команду',
                                widget=forms.Textarea,
                                required=False)
    employee3 = forms.CharField(label='Хотим в команду',
                                widget=forms.Textarea,
                                required=False)
# if add more employee fields, change forloop in save_employees in utils.py

    name = forms.CharField(label='Название проекта',
                           max_length=200)
    description = forms.CharField(label='Описание проекта',
                                  widget=forms.Textarea)
    contact_name = forms.CharField(label='Контактное лицо',
                                   max_length=50)
    slack = forms.CharField(label='Slack',
                            max_length=30)
    telegram = forms.CharField(label='Telegram',
                               max_length=30,
                               required=False)
    whatsapp = forms.CharField(label='Whatsapp',
                               max_length=30,
                               required=False)
    password = forms.CharField(label="Пароль",
                               max_length=20,
                               widget=forms.PasswordInput,
                               help_text='Цель пароля - снизить соблазн отредактировать карточку сторонними лицами. '
                                         'Используется при редактировании и удалении карточки.')

    employee1.widget.attrs.update({'class': 'form-control', 'rows': 4})
    employee2.widget.attrs.update({'class': 'form-control', 'rows': 4, 'placeholder': 'Можно оставить пустым'})
    employee3.widget.attrs.update({'class': 'form-control', 'rows': 4, 'placeholder': 'Можно оставить пустым'})
    password.widget.attrs.update({'class': 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    description.widget.attrs.update({'class': 'form-control', 'rows': 4})
    contact_name.widget.attrs.update({'class': 'form-control'})
    slack.widget.attrs.update({'class': 'form-control'})
    telegram.widget.attrs.update({'class': 'form-control', 'placeholder': 'Можно оставить пустым'})
    whatsapp.widget.attrs.update({'class': 'form-control', 'placeholder': 'Можно оставить пустым'})

    class Meta:
        model = StartupProject
        exclude = ['create_on', 'lifetime', 'upd_time', 'project_type']


class StartupProjectFormEdit(forms.ModelForm):
    """
    Форма для редактирования карточки проекта.
    Содержит все поля модели StartupProject.
    """
    name = forms.CharField(label='Название проекта',
                           max_length=200)
    description = forms.CharField(label='Описание проекта',
                                  widget=forms.Textarea)
    contact_name = forms.CharField(label='Контактное лицо',
                                   max_length=50)
    slack = forms.CharField(label='Slack',
                            max_length=30)
    telegram = forms.CharField(label='Telegram',
                               max_length=30,
                               required=False)
    whatsapp = forms.CharField(label='Whatsapp',
                               max_length=30,
                               required=False)
    password = forms.CharField(label="Пароль",
                               max_length=20,
                               widget=forms.PasswordInput,
                               help_text='Цель пароля - снизить соблазн отредактировать карточку сторонними лицами. '
                                         'Используется при редактировании и удалении карточки.')

    password.widget.attrs.update({'class': 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    description.widget.attrs.update({'class': 'form-control', 'rows': 6})
    contact_name.widget.attrs.update({'class': 'form-control'})
    slack.widget.attrs.update({'class': 'form-control'})
    telegram.widget.attrs.update({'class': 'form-control', 'placeholder': 'Можно оставить пустым'})
    whatsapp.widget.attrs.update({'class': 'form-control', 'placeholder': 'Можно оставить пустым'})

    class Meta:
        model = StartupProject
        exclude = ['create_on', 'lifetime', 'upd_time', 'project_type']


class ApplicantForm(forms.ModelForm):
    """Форма для добавления анкеты соискателя. Содержит все поля модели Applicant"""
    name = forms.CharField(max_length=200, label='Ваше имя')
    about_message = forms.CharField(label='Расскажите о себе',
                                    widget=forms.Textarea,
                                    required=False)
    skills = forms.CharField(label='Опишите ваши навыки',
                             widget=forms.Textarea)
    slack = forms.CharField(label='Slack',
                            max_length=30)
    telegram = forms.CharField(label='Telegram',
                               max_length=30,
                               required=False)
    whatsapp = forms.CharField(label='Whatsapp',
                               max_length=30,
                               required=False)
    password = forms.CharField(label="Пароль",
                               max_length=20,
                               widget=forms.PasswordInput,
                               help_text='Цель пароля - снизить соблазн отредактировать карточку сторонними лицами. '
                                         'Используется при редактировании и удалении карточки.')

    name.widget.attrs.update({'class': 'form-control'})
    about_message.widget.attrs.update({'class': 'form-control', 'rows': 6, 'placeholder': 'Можно оставить пустым'})
    skills.widget.attrs.update({'class': 'form-control', 'rows': 6})
    slack.widget.attrs.update({'class': 'form-control'})
    telegram.widget.attrs.update({'class': 'form-control', 'placeholder': 'Можно оставить пустым'})
    whatsapp.widget.attrs.update({'class': 'form-control', 'placeholder': 'Можно оставить пустым'})
    password.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Applicant
        exclude = ['create_on', 'lifetime', 'upd_time']
