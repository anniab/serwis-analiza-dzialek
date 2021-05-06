import os
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
 

from .models import World, dzialki_wszystkie_wgs

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'data','world.shp')
,)


dzialki_wszystkie_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'data','dzialki_wszystkie_wgs.shp')
,)


world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}
dzialki_wszystkie_wgs_mapping = {
    'id': 'id',
    'objectid': 'objectid',
    'identyfika': 'identyfika',
    'powierzchn': 'powierzchn',
    'teryt': 'teryt',
    'numer': 'numer',
    'obreb': 'obreb',
    'wojewodztw': 'wojewodztw',
    'powiat': 'powiat',
    'gmina': 'gmina',
    'data_od': 'data_od',
    'shape_leng': 'shape_leng',
    'shape_area': 'shape_area',
    'geom': 'MULTIPOLYGON',
}

def  run():
    lm= LayerMapping(
        World, world_shp, world_mapping,
        transform= False, encoding='iso-8859-1',
    )
    lm.save(strict= False, verbose=True)