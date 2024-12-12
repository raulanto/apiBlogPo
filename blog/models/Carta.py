from django.db import models
from django.contrib.auth.models import User


class Carta(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartas')
    titulo = models.CharField(max_length=255)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartas_recibidas')
    imagen = models.URLField(blank=True, null=True)
    contenido = models.TextField()
    posdata = models.TextField(blank=True, null=True)
    iframe = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
