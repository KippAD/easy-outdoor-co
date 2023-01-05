from django.shortcuts import render
from django.views import View


def HomePage(request):
    return render(request, 'home/index.html')