from django.shortcuts import render
from django.conf import settings


def contact(request):
    """ A view to load contact page """
    return render(request, 'contact/contact.html')
