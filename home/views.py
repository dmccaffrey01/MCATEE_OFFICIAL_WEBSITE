from django.shortcuts import render
from django.conf import settings


def index(request):
    """ A view to load home page """
    return render(request, 'home/index.html')