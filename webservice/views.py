# Create your views here.
from django.http import HttpResponse
import xmltodict, json

from django.shortcuts import render
from SourceCode.Views.run_Qutuf import runit

def index(request):
    text = request.GET.get('text', '')
    outputformat = request.GET.get('outputformat', '')
    functionality = request.GET.get('functionality', '')

    if text:
        if not outputformat:
            outputformat = 'html'
        output = runit(text, functionality, outputformat)
        if outputformat == 'xml':
            return HttpResponse(output, content_type='text/xml')
        elif outputformat == 'html':
            return HttpResponse(output, content_type='text/html')
        elif outputformat == 'json':
            o = xmltodict.parse(output)
            return HttpResponse(json.dumps(o, ensure_ascii=False).encode('utf8'), content_type='application/json')

    else:
        return render(request, 'index.html')

