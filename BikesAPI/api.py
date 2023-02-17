import requests
def get_data_bikes():
    url = "http://api.citybik.es/v2/networks/bikesantiago"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None