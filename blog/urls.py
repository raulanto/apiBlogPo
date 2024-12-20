from django.urls import path
from blog.views import cartas,poemas


app_name = 'blog'

urlpatterns = [
    path('cartas/', cartas,name='cartasvista'),
    path('poemas/', poemas,name='poemasvista'),
]
