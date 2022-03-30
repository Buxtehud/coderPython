from django.urls import path
from posts.views import inicio

urlpatterns = [
    path('index/', inicio)
]