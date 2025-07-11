from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('convert/', views.convert_images, name = 'convert_images')
]