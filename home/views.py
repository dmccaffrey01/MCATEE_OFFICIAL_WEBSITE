from django.shortcuts import render
from django.conf import settings


def index(request):
    """ A view to load home page """
    url = settings.MEDIA_URL
    context = {
        'url': url,
    }
    return render(request, 'home/index.html', context)