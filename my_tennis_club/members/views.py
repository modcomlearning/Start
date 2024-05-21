from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello World")



def local(request):
    template = loader.get_template('second.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello World")
