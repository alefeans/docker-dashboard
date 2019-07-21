from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dashboard.helpers import (list_container,
                               start_container,
                               stop_container,
                               create_container,
                               delete_container)


def containers_list(request):
    resp = list_container()
    if not resp:
        return render(request, 'dashboard/containers.html', {})

    containers = []
    for r in resp:
        container = {
            'id': r['Id'][:12],
            'name': r['Names'][0].replace('/', ''),
            'image': r['Image'],
            'status': r['Status'],
            'state': r['State']
        }
        containers.append(container)
    return render(request, 'dashboard/containers.html', {'containers': containers})  


class StartContainer(APIView):

    def post(self, request):
        try:
            container = request.data['name']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        resp = start_container(container)

        if resp:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class StopContainer(APIView):

    def post(self, request):
        try:
            container = request.data['name']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        resp = stop_container(container)

        if resp:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateContainer(APIView):

    def post(self, request):
        try:
            image = {"Image": request.data['name']}
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        created = create_container(image)
        if created:
            started = start_container(created['Id'])
            if started:
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteContainer(APIView):

    def post(self, request):
        try:
            container = request.data['name']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        resp = delete_container(container)

        if resp:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
