from django.shortcuts import render
from django.http import HttpResponse


def group(request):
    return HttpResponse("Hello Adcad group")