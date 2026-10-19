
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Producto


class HomeView(TemplateView):
    template_name = "miapp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["productos_recientes"] = Producto.objects.order_by("-id")[:3]

        # Conservamos la variable para la plantilla
        context["user_logged"] = self.request.user.is_authenticated

        return context

def acerca_de_mi(request):
    return render(request, "miapp/acerca-de-mi.html")


class CatalogoView(ListView):
    model = Producto
    template_name = "miapp/catalogo.html"
    context_object_name = "productos"


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "miapp/detalle.html", {"producto": producto})
