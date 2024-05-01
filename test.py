import requests

ENDPOINT_URL = 'https://cgcom-interno.cgcom.es/RegistroMedicos/PUBBusquedaPublica_busqueda_ajax.action'

cookies = {
    'JSESSIONID': '89CE33663A67433CA0ACB9EDD33FA884',
}

data = {
    'numeroColegiado': '080843771',
    'nombre': 'Jaime',
    'Apellido1': 'Gonzalez',
    'Apellido2': '',
    'idEspecialidad': '',
    'idProvincia': '',
    'codigoCaptcha': '8765e',
}

response = requests.post(
    ENDPOINT_URL,
    cookies=cookies,
    data=data,
)

print(response.text)

