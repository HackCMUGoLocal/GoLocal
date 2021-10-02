from django.urls import path
from . import views


urlpatterns = [
  path('form/', views.formPage, name='form'),
  path('', views.mainPage, name='index')
]
