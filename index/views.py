#from _future_ import unicode_literals

from django.shortcuts import render

from .models import World, dzialki_wszystkie_wgs,dzialki_wszystkie_wgs_dobre, dzialki_razem_wgs_dobre,dzialki_slope_wgs, dzialki_aspect_wgs_dobre
from django.http import HttpResponse
from django.core.serializers import serialize

# Create your views here.
def index(request):
    return render(request, 'index.html')


def slope(reqest):
    slope=dzialki_slope_wgs.objects.all()
    geojson=serialize('geojson',slope,geometry_field='geom', fields=('id','geom','numer', 'pole_ar','obwod'))
    return HttpResponse(geojson,content_type='json')
    
def dzialkiwszystkiewgsdobre(reqest):
    dzialkiwszystkiewgs=dzialki_wszystkie_wgs_dobre.objects.all()
    geojson=serialize('geojson',dzialkiwszystkiewgs, geometry_field='geom', fields=('id','geom','numer', 'pole_ar','obwod'))
    return HttpResponse(geojson,content_type='json')  
    
def dzialkirazemwgsdobre(reqest):
    dzialkirazemwgs=dzialki_razem_wgs_dobre.objects.all()
    geojson=serialize('geojson', dzialkirazemwgs, geometry_field='geom', fields=('id','geom','numer', 'pole_ar','obwod'))
    return HttpResponse(geojson,content_type='json') 
    
def dzialkiaspectwgsdobre(reqest):
    dzialkiaspectwgs=dzialki_aspect_wgs_dobre.objects.all()
    geojson=serialize('geojson', dzialkiaspectwgs, geometry_field='geom', fields=('id','geom','numer', 'pole_ar','obwod'))
    return HttpResponse(geojson,content_type='json')  

    
def index2(request):
    return render(request, 'index2.html')
    
def korzystanie(request):
    return render(request, 'korzystanie.html')
    
def algorytmy(request):
    return render(request, 'algorytmy.html')
    
def stwo_analiza(request):
    return render(request, 'stwo_analiza.html')