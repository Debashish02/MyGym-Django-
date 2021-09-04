from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.blog,name="home"),
    path('contact/',views.create_contact,name="contact"),
    path('about-us/',views.about,name="about"),
    path('login/',views.login,name="login")
]
