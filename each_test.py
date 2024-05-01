import requests

cookies = {
    'JSESSIONID': '5B28C1353CD272BBBDC0115B6E5F2514',
}



params = {
    'numeroColegiado': '282860336',
}

c = 1
while True:

    response = requests.get(
        'https://cgcom-interno.cgcom.es/RegistroMedicos/PUBBusquedaPublica_busquedaDetalle_ajax.action',
        params=params,
        cookies=cookies,

    )

    print(c, end=' ')
    c += 1

    if response.status_code == 200:
        if 'JAIME VICENTE' in response.text:
            print('ok')
            continue

    print('bad')

