from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

class ProductosTemplateView(TemplateView):
    template_name = "productos.html"

def home_1 (request):
    return HttpResponse ("<h1>Bienvenidos a Tienda Libre</h1>")

def home (request):
    return render(request, "home.html")