from django.http import HttpResponse
from django.shortcuts import render
import requests


# Create your views here.

def get_data_bikes(request):
    url = "https://api.citybik.es/v2/networks/bikesantiago"
    response = requests.get(url)
    return HttpResponse(response)
