from django.db import models
from ckeditor.fields import RichTextField
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(verbose_name="Fecha de creaciónn", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name="Página"
        verbose_name_plural="Páginas"
        ordering = ['title']

    def __str__(self):
        return self.title