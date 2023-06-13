from django.urls import path
from lookup import views

urlpatterns = [
    path("home/", view=views.home, name="home"),
    path("aboutme/", view=views.about_me, name="aboutme"),
]
