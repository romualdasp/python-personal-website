from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_preview, name='cv_preview'),
    path('clear/', views.clear_db, name='clear_db'),
]
