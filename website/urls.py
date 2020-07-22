from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='index'),
    path('all_cards/', views.AllCardsView.as_view(), name='all_cards_list'),
    path('new_applicant/', views.new_applicant, name='new_applicant'),
    path('applicants/', views.ApplicantView.as_view(), name='applicants_list'),
    path('projects/', views.ProjectView.as_view(), name='projects_list'),
    path('new_project/<project_type>/', views.new_project, name='new_project'),
    path('access_check/p/<int:startup_id>/', views.project_access_check, name='project_access_check'),
    path('access_check/a/<int:applicant_id>/', views.applicant_access_check, name='applicant_access_check'),
    path('edit_project/<int:startup_id>/', views.edit_project, name='edit_project'),
    path('edit_applicant/<int:applicant_id>/', views.edit_applicant, name='edit_applicant'),
    path('delete_project/<int:startup_id>/', views.delete_project, name='delete_project'),
    path('delete_applicant/<int:applicant_id>/', views.delete_applicant, name='delete_applicant')
]


# TODO: sentry
