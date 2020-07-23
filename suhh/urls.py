from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('website.urls')),
    path('adminpage/', admin.site.urls),
]

handler404 = 'website.views.not_found'
handler403 = 'website.views.permission_denied'
