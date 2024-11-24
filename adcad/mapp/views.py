from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# def group(request):
#     return HttpResponse("Hello Adcad group")

def group(request):
    template = loader.get_template('mapp/index.html')
    return HttpResponse(template.render())
    