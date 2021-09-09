from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnedobject = HttpResponse('hello world')
    return returnedobject

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'