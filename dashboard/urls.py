from django.urls import path
from .views import container_list, image_list, redirect_view, StopContainer, StartContainer, CreateContainer, DeleteContainer, DeleteImage

urlpatterns = [
    path('', redirect_view, name='redirect_view'),
    path('images', image_list, name='image_list'),
    path('containers', container_list, name='container_list'),
    path('stop_container', StopContainer.as_view(), name='stop_container'),
    path('start_container', StartContainer.as_view(), name='start_container'),
    path('create_container', CreateContainer.as_view(), name='create_container'),
    path('delete_container', DeleteContainer.as_view(), name='delete_container'),
    path('delete_image', DeleteImage.as_view(), name='delete_image'),
]
