"""
Definition of urls for Sentences.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('project1a/', views.project1a, name='project1a'),
    path('project1b/', views.project1b, name='project1b'),
    path('project2/', views.project2, name='project2'),
    # path('project3/', views.project3, name='project3'),
    # path('project4/', views.project4, name='project4'),
    path('project3/', views.project3, name='project3'),
    path('project4/', views.project4, name='project4'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)