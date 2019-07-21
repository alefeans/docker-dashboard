from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.redirect_view, name='redirect_view'),
    path('images', views.images_list, name='images_list'),
    path('images/delete', views.DeleteImage.as_view(), name='delete_images'),
    path('images/pull', views.PullImage.as_view(), name='pull_images'),
    path('containers', views.containers_list, name='containers_list'),
    path('containers/stop', views.StopContainer.as_view(), name='stop_containers'),
    path('containers/start', views.StartContainer.as_view(), name='start_containers'),
    path('containers/create', views.CreateContainer.as_view(), name='create_containers'),
    path('containers/delete', views.DeleteContainer.as_view(), name='delete_containers'),
]
