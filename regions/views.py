from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import County, Headquarter, RegionalOffice, FieldOffice
# Create your views here.

class HomePageView(TemplateView):
    template_name='index.html'


def county_datasets(request):
    counties = serialize('geojson', County.objects.all())

    return HttpResponse(counties, content_type='json')

def headquarter_datasets(request):
    headquarters = serialize('geojson', Headquarter.objects.all())

    return HttpResponse(headquarters, content_type='json')

def regionaloffice_datasets(request):
        regionaloffice = serialize('geojson', RegionalOffice.objects.all())

        return HttpResponse(regionaloffice, content_type='json')
def fieldoffice_datasets(request):
        fieldoffice = serialize('geojson', FieldOffice.objects.all())

        return HttpResponse(fieldoffice, content_type='json')