from django.urls import path
from . import views

urlpatterns = [
  path('', views.getRoutes),
  path('stores/', views.getStores),
  path('stores/<str:pk>/', views.getStore),
  path('products/', views.getProducts),
  path('products/<str:pk>/', views.getProduct),
]
