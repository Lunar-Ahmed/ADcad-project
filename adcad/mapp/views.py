from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Group


# def group(request):
#     return HttpResponse("Hello Adcad group")

# def group(request):
#     template = loader.get_template('mapp/index.html')
#     return HttpResponse(template.render())

def group(request):
  mygroup = Group.objects.all().values()
  template = loader.get_template('mapp/index.html')
  context = {
    'mygroup': mygroup,
  }
  return HttpResponse(template.render(context, request))
    
    
def details(request, id):
    mystaff = Group.objects.get(id=id)
    template = loader.get_template('mapp/details.html')
    context = {
        'mystaff': mystaff,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('mapp/main.html')
  return HttpResponse(template.render())