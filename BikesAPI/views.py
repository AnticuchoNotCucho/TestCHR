from django.http import HttpResponse
from django.shortcuts import render
import requests

from BikesAPI.models import Extra, Station, Network, Location


# Create your views here.

def get_data_bikes(request):
    print('Obteniendo datos...')
    # Obtener los datos de la API usando requests o alguna librería similar
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    data = response.json()
    network = data['network']
    location = data['network']['location']
    location_instance = Location.objects.create(**location)
    network['location'] = location_instance
    network_instance = Network.objects.create(
        company=network['company'],
        gbfs_href=network['gbfs_href'],
        href=network['href'],
        id=network['id'],
        location=location_instance,
        name=network['name']
    )
    stations_data = data['network']['stations']
    # Crear instancias del modelo Station a partir de los datos obtenidos
    for station_data in stations_data:
        # Validar si ya existe una instancia de Station con el mismo id
        if not Station.objects.filter(id=station_data['id']).exists():
            # Crear instancia del modelo Extra a partir de los datos de 'extra'
            post_code = station_data['extra'].get('post_code', None)
            if post_code is None:
                post_code = 'N/A'
            extra_instance = Extra.objects.create(
                address=station_data['extra']['address'],
                altitude=station_data['extra']['altitude'],
                ebikes=station_data['extra']['ebikes'],
                has_ebikes=station_data['extra']['has_ebikes'],
                last_updated=station_data['extra']['last_updated'],
                normal_bikes=station_data['extra']['normal_bikes'],
                payment=station_data['extra']['payment'],
                payment_terminal=station_data['extra']['payment-terminal'],
                post_code=post_code,
                renting=station_data['extra']['renting'],
                returning=station_data['extra']['returning'],
                slots=station_data['extra']['slots'],
                uid=station_data['extra']['uid']
            )
            # Crear instancia del modelo Station a partir de los datos de la estación
            station_data['extra'] = extra_instance
            station_instance = Station.objects.create(**station_data)

        # Retornar una respuesta
    return HttpResponse("Datos guardados en la base de datos")
