from django.http import HttpResponse

from front.models import Demo

def index(request):
    d = Demo(name='Beatles Blog')
    d.save()
    return HttpResponse("Hello, world. You're at the polls index.")

