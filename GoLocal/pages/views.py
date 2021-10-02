from django.shortcuts import render
import requests


# Create your views here.
def mainPage(request):
  resp = requests.get(url="http://127.0.0.1:8000/stores")
  store_list = resp.json()

  resp = requests.get(url="http://127.0.0.1:8000/products")
  product_list = resp.json()

  return render(request, "index.html", {"store_list": store_list, "product_list": product_list})