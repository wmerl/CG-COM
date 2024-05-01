import requests

from vars import RequestsVars

cookies = {
    'JSESSIONID': RequestsVars.JSESSIONID,
}


data = {
    'numeroColegiado': '080843771',
    'nombre': 'Jaime',
    'Apellido1': 'Gonzalez',
    'Apellido2': '',
    'idEspecialidad': '',
    'idProvincia': '08',
    'codigoCaptcha': 'b6rwg',
}

response = requests.post(
    'https://cgcom-interno.cgcom.es/RegistroMedicos/PUBBusquedaPublica_busqueda_ajax.action',
    cookies=cookies,
    data=data,
)

print(response)

