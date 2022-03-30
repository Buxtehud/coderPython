from django.http import HttpResponse
from django.template import loader


def inicio(request):
    template = loader.get_template('index.html')
    document = template.render()
    return HttpResponse(document)
