from django.urls import path
from posts.views import inicio

urlpatterns = [
    path('', inicio, name='Inicio')
]