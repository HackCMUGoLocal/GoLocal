from django.shortcuts import render
import requests


# Create your views here.
def mainPage(request):return render(request, 'index.html')
def formPage(request):return render(request, 'form.html')