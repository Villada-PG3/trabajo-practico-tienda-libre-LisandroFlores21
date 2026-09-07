# Consultas de clase 5 


## 1.
todos = Producto.objects.all()
## 2.
primer_prod = Producto.objects.first()
## 3.
ordenados = Producto.objects.order_by("-precio")
## 4.
mas_caros = Producto.objects.filter(precio__gt=10000)
## 5.
mas_baratos = Producto.objects.filter(precio__lte=5000)
## 6.
busqueda = Producto.objects.filter(nombre__icontains="auricular")
## 7.
prods_teclado = Producto.objects.filter(nombre__icontains="teclado")
## 8.
prod_unico = Producto.objects.get(id=1)
## 9.
p = Producto.objects.first()
categoria_del_producto = p.categoria.nombre
## 10.
nueva_cat, _ = Categoria.objects.get_or_create(nombre="Tecnología")
nuevo_p = Producto.objects.create(
    nombre="Heladera",
    precio=200000,
    stock=2,
    categoria=nueva_cat
)