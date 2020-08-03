# from celery import shared_task
# from itertools import chain
# from .models import StartupProject, Applicant
# from datetime import datetime, timedelta
#
#
# @shared_task
# def delete_expired_database_records():
#     now = datetime.now().date()
#     startup_queryset = StartupProject.objects.all()
#     applicant_queryset = Applicant.objects.all()
#     for record in chain(startup_queryset, applicant_queryset):
#         if record.create_on.date() + timedelta(days=record.lifetime) <= now:
#             with open('celery_log.txt', 'a', encoding='utf-8') as file:
#                 print(f'{datetime.now()}: {record.__class__.__name__} - {record.id} - {record.create_on} - {record.lifetime} deleted',
#                       file=file)
#             record.delete()
