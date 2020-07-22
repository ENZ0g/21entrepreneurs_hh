from django.db import models


class StartupProject(models.Model):
    """The table containing info about the startup."""
    upd_time = models.DateTimeField('Время последнего изменения', auto_now=True)
    project_type = models.CharField('Тип проекта', max_length=8)
    name = models.CharField(max_length=200, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    contact_name = models.CharField(max_length=50, verbose_name='Контактное лицо')
    slack = models.CharField(max_length=30)
    telegram = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=20)


class Employee(models.Model):
    """The table containing info about what employees are needed for startup."""
    startup = models.ForeignKey(StartupProject,
                                on_delete=models.CASCADE,
                                verbose_name='Название проекта',
                                related_name='employees')
    employee = models.TextField(verbose_name='Xотим в командy')


class Applicant(models.Model):
    """The table containing info about applicants."""
    upd_time = models.DateTimeField('Время последнего изменения', auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Имя соискателя')
    about_message = models.TextField('О себе', blank=True)
    skills = models.TextField('Навыки')
    slack = models.CharField(max_length=30)
    telegram = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=20)
