from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Excuse the mess we are rebuilding.")
