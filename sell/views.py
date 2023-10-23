from django.shortcuts import render
from django.conf import settings


def sell(request):
    """ A view to load sell page """
    return render(request, 'sell/sell.html')
