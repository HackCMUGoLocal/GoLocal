from django.urls import path
from . import views

urlpatterns = [
  path('', views.getRoutes),
  path('stores/', views.getStore)
  path('products/', views.getProduct)
]
