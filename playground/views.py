from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#view function takes res/req
#request handler



def hello(request):
    return render(request, 'hello.html', {'name': 'Owen'})