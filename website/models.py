from django.db import models


class StartupProject(models.Model):
    """The table containing info about the startup."""
    create_on = models.DateTimeField('Время создания', auto_now_add=True)
    lifetime = models.SmallIntegerField('Время жизни записи')
    upd_time = models.DateTimeField('Время последнего изменения', auto_now=True)  # require for sorting cards in views
    project_type = models.CharField('Тип проекта', max_length=8)
    name = models.CharField('Название проекта', max_length=200)
    description = models.TextField('Описание проекта')
    contact_name = models.CharField('Контактное лицо', max_length=50)
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
    create_on = models.DateTimeField('Время создания', auto_now_add=True)
    lifetime = models.SmallIntegerField('Время жизни записи')
    upd_time = models.DateTimeField('Время последнего изменения', auto_now=True)
    name = models.CharField('Имя соискателя', max_length=200)
    about_message = models.TextField('О себе', blank=True)
    skills = models.TextField('Навыки')
    slack = models.CharField(max_length=30)
    telegram = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=20)
