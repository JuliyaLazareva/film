from django.urls import path, include
from .views import index

app_name = 'my_films'

urlpatterns = [
    path('', index, name='index')
]