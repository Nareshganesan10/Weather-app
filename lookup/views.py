from django.shortcuts import render
import json
import requests
from django.views.decorators import csrf
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie

from lookup.models import CityModel
from lookup.serilaizers import CitySerializer

def home(request):
    city_list = CityModel.objects.all()
    if request.method == 'GET':
        return render(request, "home.html", {})
    elif request.method == "POST":
        city = request.POST['City']
        api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=653feb430778453ab6d60823231406&q="+ str(city) + "&aqi=yes")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error"
    print(api)
    return render(request, "home.html", {
        "api": api,
        "city_list": city_list,
        })

def about_me(request):
    return render(request, "aboutme.html", {})
