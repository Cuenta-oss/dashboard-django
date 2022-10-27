from django.db import models

class categoriaProducto(models.Model):
    categoria = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'categoriaProducto'
        verbose_name_plural = 'categoriaProductos'

    def __str__(self):
        return self.categoria


class infoProducto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=200)
    disponibilidad = models.BooleanField()
    categoriaProduct = models.ForeignKey(
        categoriaProducto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'infoProducto'
        verbose_name_plural = 'infoProductos'

    def __str__(self):
        return self.nombre

gender_list = [
    [0, "Masculino"],
    [1, "Femenino"],
    [2, "Otro"],
]


class contact(models.Model):

    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    sexo = models.IntegerField(choices=gender_list, default=0)

    def __str__(self):
        self.nombre
