from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('accounts/', views.projects, name='projects'),
    path('feedback/', views.add_feedback, name='add_feedback'),
]