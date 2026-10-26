from .models import Categoria


def categorias_processor(request):
    return {
        "categorias_list": Categoria.objects.all()
    }