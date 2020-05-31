from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_preview, name='cv_preview'),
    path('skill/new/', views.skill_new, name='skill_new'),
    path('skill/remove/<pk>/', views.skill_remove, name='skill_remove'),
]
