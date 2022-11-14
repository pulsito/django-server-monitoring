from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


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


@login_required(login_url='/profile /login/')
def secure(request):
    return render(request, 'secure.html')