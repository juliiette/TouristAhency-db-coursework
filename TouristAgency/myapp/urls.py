from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tourists_all', views.tourists_all)
]


