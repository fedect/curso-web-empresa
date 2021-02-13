from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now=True)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering = ['created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content =models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name= 'Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categoria", related_name="get_posts")
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now=True)
    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering = ['created']

    def __str__(self):
        return self.title
