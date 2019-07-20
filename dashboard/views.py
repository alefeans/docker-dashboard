from django.http import HttpResponseRedirect
from django.shortcuts import render
from requests_unixsocket import Session
from docker_dashboard.settings import DOCKER_API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class StopContainer(APIView):

    def post(self, request):
        container = request.data['name']
        session = Session()
        resp = session.post(DOCKER_API + 'containers/{}/stop'.format(container))
        if resp.status_code == 204:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class StartContainer(APIView):

    def post(self, request):
        container = request.data['name']
        session = Session()
        resp = session.post(DOCKER_API + 'containers/{}/start'.format(container))
        if resp.status_code == 204:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateContainer(APIView):

    def post(self, request):
        image = request.data['name']
        session = Session()
        data = {
            "Image": image
        }
        resp = session.post(DOCKER_API + 'containers/create', json=data)
        if resp.status_code == 201:
            container_id = resp.json()['Id']
            resp = session.post(DOCKER_API + 'containers/{}/start'.format(container_id))
            if resp.status_code == 204:
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteContainer(APIView):

    def post(self, request):
        container = request.data['name']
        session = Session()
        resp = session.delete(DOCKER_API + 'containers/{}?force=True'.format(container))
        if resp.status_code == 204:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteImage(APIView):

    def post(self, request):
        container = request.data['name']
        session = Session()
        resp = session.delete(DOCKER_API + 'images/{}?force=True'.format(container))
        if resp.status_code == 200:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
