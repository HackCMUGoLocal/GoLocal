from django.urls import path
from . import views

urlpatterns = [
  path('', views.getRoutes),
  path('stores/', views.getStores),
  path('stores/create/', views.createStore),
  path('stores/<str:pk>/delete/', views.deleteStore),
  path('stores/<str:pk>/', views.getStore),
]
