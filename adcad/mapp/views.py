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

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))


from django.shortcuts import render, redirect
from .models import InputTable # Ensure Teacher model is imported
from .forms import InputTableForm

def table_view(request):
    # Fetch all teacher names
    teachers = Group.objects.all().values()
    input_table = InputTable.objects.first()  # Get the first record
    if not input_table:
        input_table = InputTable.objects.create()

    if request.method == 'POST':
        form = InputTableForm(request.POST, instance=input_table)
        if form.is_valid():
            form.save()
            return redirect('table_view')
    else:
        form = InputTableForm(instance=input_table)

    context = {
        'form': form,
        'total': input_table.total(),
        'teachers': teachers,
    }

    return render(request, 'mapp/table.html', context)

