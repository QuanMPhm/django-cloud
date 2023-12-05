from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):

    template = loader.get_template("cloud/login.html")
    context = {
        'user' : 1
    }
    return HttpResponse(template.render(context, request))