import json

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

from ServiceEnvironmentAPI.models import Proyecto


def get_data_scrapped():
    print('extrayendo datos...')
    response = requests.get('https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php')
    soup = BeautifulSoup(response.content, 'html.parser')
    div_info = soup.find('div', {'id': 'info_resultado'}).text
    wordforindex = 'Número de páginas:'
    index = div_info.find(wordforindex)
    pages = int(div_info[index + len(wordforindex):len(div_info)].strip().replace(',', ''))
    data = []

    def get_projects(page_num):
        url = f'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_fila_actual={page_num}'
        response_page = requests.get(url)
        soup_page = BeautifulSoup(response_page.content, 'html.parser')
        rows = soup_page.find('table', class_='tabla_datos').find('tbody').findAll('tr')
        for tr in rows:
            columns = tr.findAll('td')
            project = Proyecto(
                numero=columns[0].text,
                nombre=columns[1].text,
                tipo=columns[2].text,
                region=columns[3].text,
                titular=columns[4].text,
                tipologia=columns[5].text,
                inversion=columns[6].text,
                fecha=columns[7].text,
                estado=columns[8].text
            )
            data.append({
                'numero': project.numero,
                'nombre': project.nombre,
                'tipo': project.tipo,
                'region': project.region,
                'titular': project.titular,
                'tipologia': project.tipologia,
                'inversion': project.inversion,
                'fecha': project.fecha,
                'estado': project.estado
            })
            project_instance = Proyecto.objects.create(
                numero=project.numero,
                nombre=project.nombre,
                tipo=project.tipo,
                region=project.region,
                titular=project.titular,
                tipologia=project.tipologia,
                inversion=project.inversion,
                fecha=project.fecha,
                estado=project.estado
            )
    with ThreadPoolExecutor(max_workers=16) as executor:
        executor.map(get_projects, range(1, 10 + 1))
    with open('proyectos.json', 'a', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print('extraccion de datos realizada')
