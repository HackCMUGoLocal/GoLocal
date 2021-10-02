from django.shortcuts import render
import requests


# Create your views here.
def mainPage(request):
  resp = '[{"id":1,"name":"Giant Eagle","location":"123 Main St, Pittsburgh, Pennsylvania","phone":"1234567890","website":"gianteagle.com","hoursOfOperation":10},{"id":3,"name":"Target","location":"123 Main St, Pittsburgh, Pennsylvania","phone":"1234567890","website":"gianteagle.com","hoursOfOperation":10}]'
  store_list = resp.json()

  resp = '[{"id":1,"name":"bread","price":5,"store":[1]},{"id":2,"name":"bread","price":5,"store":[1]}]'
  product_list = resp.json()

  return render(request, "index.html", {"store_list": store_list, "product_list": product_list})