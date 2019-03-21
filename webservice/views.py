# Create your views here.
from django.http import HttpResponse
import xmltodict, json

from django.shortcuts import render
from SourceCode.Views.run_Qutuf import runit

def index(request):
    """The home page for learning log"""
    phrase = request.GET.get('phrase', '')
    type = request.GET.get('type', '')

    if phrase and type:
        output = runit(phrase, type)
        if type == 'xml':
            return HttpResponse(output, content_type='text/xml')
        elif type == 'html':
            return HttpResponse(output, content_type='text/html')
        elif type == 'json':
            o = xmltodict.parse(output)
            return HttpResponse(json.dumps(o, ensure_ascii=False).encode('utf8'), content_type='application/json')

    else:
        return render(request, 'index.html')

