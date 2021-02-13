from django.db import models

class Services(models.Model):
    Title = models.CharField(max_length=200, verbose_name='Título')
    Subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    Content = models.TextField(verbose_name='Contenido')
    Image = models.ImageField(verbose_name='Imagen', upload_to='Services')
    Created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    Updated = models.DateTimeField(verbose_name='Actualizado', auto_now=True)

class Meta:
    verbose_name='Servicio'
    verbose_name_plural='Servicios'
    ordering = ['created']

def __str__(self):
    return self.Title
