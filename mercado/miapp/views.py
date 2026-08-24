from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

class ProductosTemplateView(TemplateView):
    template_name = "productos.html"

def home(request):
    return render(request, 'miapp/home.html')

# Vista para la tarea "Acerca de mí"
def acerca_de_mi(request):
    return render(request, 'miapp/acerca-de-mi.html')

