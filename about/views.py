from django.shortcuts import render
from django.conf import settings


def about(request):
    """ A view to load about page """
    return render(request, 'about/about.html')
