from django.shortcuts import render
from django.conf import settings


def coaching(request):
    """ A view to load coaching page """
    return render(request, 'coaching/coaching.html')
