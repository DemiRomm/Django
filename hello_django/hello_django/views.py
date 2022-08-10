from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 10*9
    return render(request, 'about.html', {'greeting':a})

def home(request):
    return HttpResponse('This is my home')
