from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('home/', views.home_page, name='home'),
    path('contacts/', views.contacts_page, name='contacts'),
]

