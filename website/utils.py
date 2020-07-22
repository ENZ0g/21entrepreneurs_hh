from .models import Employee
from .slack_tmpl import get_new_project_message, get_new_applicant_message
import re
import requests
import json
import os


def save_employees(startup, form):
    """Add new employees from StartupProjectFormNew in Employee database"""
    employees_list = []
    for i in range(1, 4):  # <-- by the number of employee fields in StartupProjectFormNew in forms.py
        employee = form.cleaned_data[f'employee{i}']
        if employee:
            Employee.objects.create(
                startup=startup,
                employee=employee
            )
            employees_list.append(employee)
    return employees_list


def request_is_correct(request):
    """Check that the transition to the page was by the link, not by direct address."""
    allowed_referers = ['all_cards', 'edit_project', 'projects', 'edit_applicant', 'applicants']
    regexp = re.compile(r'/[a-z_]+/')
    match = regexp.search(request.META.get('HTTP_REFERER', ''))
    if match is not None and match.group().strip('/') in allowed_referers:
        return True
    else:
        return False


def get_current_referrer(request):
    """Return referrer for the current page with added _list"""
    return request.META.get('HTTP_REFERER').split('/')[-2] + '_list'


def send_new_project_to_slack(startup, employees_list, link):
    """Send message with info about new project to Slack"""
    url = os.environ.get('SLACK_URL')
    data = json.dumps(get_new_project_message(startup, employees_list, link))
    requests.post(url, headers={'Content-type': 'application/json'}, data=data)
    requests.post('192.168.0.106:8080/json', headers={'Content-type': 'application/json'}, data=data)


def send_new_applicant_to_slack(applicant, link):
    """Send message with info about new applicant to Slack"""
    url = os.environ.get('SLACK_URL')
    data = json.dumps(get_new_applicant_message(applicant, link))
    requests.post(url, headers={'Content-type': 'application/json'}, data=data)
