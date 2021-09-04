from django.urls import path
from . import views

urlpatterns = [
    path('gym/', views.gym),
    path('workout/', views.gym),
]