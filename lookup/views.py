from django.shortcuts import render
import json
import requests
from django.views.decorators import csrf
# Create your views here.

#http://api.weatherstack.com/current?access_key=be85b86fb0c2beb5b0b9244d2903db8d&query=New York
def home(request):
    if request.method == "POST":
        city = request.POST['City']
        api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=9ac471934a0b45468c761301230706&q="+ str(city) + "&aqi=yes")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "error"
    return render(request, "home.html", {"api": api})

def about_me(request):
    return render(request, "aboutme.html", {})