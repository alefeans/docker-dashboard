from django.urls import path
from .views import container_list, image_list, redirect_view

urlpatterns = [
    path('', redirect_view, name='redirect_view'),
    path('images', image_list, name='image_list'),
    path('containers', container_list, name='container_list')
]
