from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the gimnasia index.")

def detail(request, entrenador_id):
    return HttpResponse("You're looking at entrenador %s." % entrenador_id)

def results(request, entrenador_id):
    response = "You're looking at the results of entrenador %s."
    return HttpResponse(response % entrenador_id)

def vote(request, entrenador_id):
    return HttpResponse("You're voting on entrenador %s." % entrenador_id)