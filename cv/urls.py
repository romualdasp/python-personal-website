from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_preview, name='cv_preview'),
    path('skill/<pk>/remove/', views.skill_remove, name='skill_remove'),
    path('clear/', views.clear_db, name='clear_db'),
]
