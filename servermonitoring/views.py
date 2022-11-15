from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import ServerSerializer, ServerLocationSerializer


def index(request):
    servers = ServerMonitoring.objects.all()
    return render(request, 'index.html', {'servers': servers})


def get_server_info(request, id):
    try:
        server = ServerMonitoring.objects.get(id=id)
        server = [(str(k).capitalize().replace('_', ' '), v) for k, v in server.__dict__.items()]
    except ObjectDoesNotExist:
        return HttpResponse("Sorry, wrong id")
    return render(request, 'server_info.html', {'server': server[1:]})


@login_required(login_url='/profile/login/')
def secure(request):
    return render(request, 'secure.html')


class ServersAPIView(APIView):
    def get(self, request):
        queryset = ServerMonitoring.objects.all()
        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServerAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            queryset = ServerMonitoring.objects.get(id=id)
            serializer = ServerSerializer(queryset)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class ServerLocationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs['id']
            queryset = ServerMonitoring.objects.get(id=id)
            serializer = ServerLocationSerializer(queryset)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class FilesAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.FILES)
        file = request.FILES['csv']
        file_name = default_storage.save(file.name, file)
        response = {
            file_name: 'saved'
        }
        return Response(response)
