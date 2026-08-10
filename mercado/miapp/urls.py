from django.urls import path
from . import views

app_name = "TiendaLibre"

urlpatterns = [
    path("", views.home, name="home"),
]
