from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.redirect_view, name='redirect_view'),
    path('images', views.image_list, name='image_list'),
    path('containers', views.container_list, name='container_list'),
    path('stop_container', views.StopContainer.as_view(), name='stop_container'),
    path('start_container', views.StartContainer.as_view(), name='start_container'),
    path('create_container', views.CreateContainer.as_view(), name='create_container'),
    path('delete_container', views.DeleteContainer.as_view(), name='delete_container'),
    path('delete_image', views.DeleteImage.as_view(), name='delete_image'),
]
