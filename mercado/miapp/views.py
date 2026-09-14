from django.shortcuts import render
from .models import Producto
from django.shortcuts import get_object_or_404


def home(request):
    productos = [
    {
        "nombre": "Notebook Lenovo",
        "precio": None,
        "categoria": "Informática",
        "stock": 3,
    },
    {
        "nombre": "Teclado mecánico",
        "precio": 75000,
        "categoria": "Periféricos",
        "stock": 12,
    },
    {
        "nombre": "Mouse Logitech",
        "precio": 45000,
        "categoria": "Periféricos",
        "stock": 20,
    },
    {
        "nombre": "Monitor Samsung",
        "precio": 280000,
        "categoria": "Monitores",
        "stock": 0,
    },
    {
        "nombre": "Auriculares Sony",
        "precio": 120000,
        "categoria": "Audio",
        "stock": 7,
    },
    {
        "nombre": "Webcam Logitech",
        "precio": 95000,
        "categoria": "Accesorios",
        "stock": 15,
    },
]

    user_logged = True

    contexto = {
        "productos": productos,
        "user_logged": user_logged,
    }

    return render(request, "miapp/home.html", contexto)

def acerca_de_mi(request):
    return render(request, "miapp/acerca-de-mi.html")

def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by("stock")
    context = {"productos": productos}
    return render(request, "miapp/catalogo.html", context)

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {"producto": producto}
    return render(request, "miapp/detalle.html", context)