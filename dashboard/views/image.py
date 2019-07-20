from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dashboard.helpers import list_image, delete_image


def redirect_view(request):
    return HttpResponseRedirect('/images')


def image_list(request):
    resp = list_image()
    if not resp:
        return render(request, 'dashboard/image_list.html', {})

    images = []
    for res in resp:
        for r in res['RepoTags']:
            full_name = r.split('/')
            name, tag = full_name[-1].split(':')
            image = {
                'repo': '/'.join(full_name[:2]),
                'name': name,
                'tag': tag
            }
            images.append(image)
    return render(request, 'dashboard/image_list.html', {'images': images})


class DeleteImage(APIView):

    def post(self, request):
        try:
            image = request.data['name']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        resp = delete_image(image)
        if resp:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
