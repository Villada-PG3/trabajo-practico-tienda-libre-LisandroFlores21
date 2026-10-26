
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Categoria, Producto
from django.db.models import Q

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
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(nombre__icontains=q) |
                Q(descripcion__icontains=q) |
                Q(marca__icontains=q)
            )

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context

class CategoriaView(ListView):
    model = Producto
    template_name = "miapp/categoria.html"
    context_object_name = "productos"
    paginate_by = 6

    def get_queryset(self):
        self.categoria = get_object_or_404(Categoria, slug=self.kwargs["slug"])
        return Producto.objects.filter(categoria=self.categoria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoria"] = self.categoria
        return context



class ProductoDetailView(DetailView):
    model = Producto
    template_name = "miapp/detalle.html"
    context_object_name = "producto"
