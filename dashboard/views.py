from django.http import HttpResponseRedirect
from django.shortcuts import render
from requests_unixsocket import Session
from docker_dashboard.settings import DOCKER_API


def redirect_view(request):
    return HttpResponseRedirect('/images')


def image_list(request):
    session = Session()
    response = session.get(DOCKER_API + 'images/json')
    images = []
    for resp in response.json():
        for r in resp['RepoTags']:
            full_name = r.split('/')
            name, tag = full_name[-1].split(':')
            image = {
                'repo': '/'.join(full_name[:2]),
                'name': name,
                'tag': tag
            }
            images.append(image)
    return render(request, 'dashboard/image_list.html', {'images': images})


def container_list(request):
    session = Session()
    response = session.get(DOCKER_API + 'containers/json?all=True')
    containers = []
    for resp in response.json():
        container = {
            'id': resp['Id'][:13],
            'name': resp['Names'][0].replace('/', ''),
            'image': resp['Image'],
            'status': resp['Status']
        }
        containers.append(container)
    return render(request, 'dashboard/container_list.html', {'containers': containers})


def stop_container(request):
    pass