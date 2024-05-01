import asyncio
import time

import aiohttp

from asyncio import Task
from typing import Any
from vars import RequestsVars


async def fetch(s, user_data: dict[str: str]) -> Any:

    endpoint_url = RequestsVars.ENDPOINT_URL

    cookies = {
        'JSESSIONID': RequestsVars.JSESSIONID,
    }

    async with s.post(endpoint_url, data=user_data, cookies=cookies) as r:
        # print(r.status)
        if r.status != 200:
            #r.raise_for_status()
            return None
        return await r.text()


async def fetch_all(s, users_data: dict[str: str]) -> tuple[Any]:

    tasks: list[Task[dict]] = []
    for _ in range(10):
        task: Task = asyncio.create_task(fetch(s, users_data))
        tasks.append(task)
    res: tuple[Any] = await asyncio.gather(*tasks)
    return res


async def get_users_data(users_data: dict[str: str]) -> tuple[Any]:

    async with aiohttp.ClientSession() as session:
        json_data = await fetch_all(session, users_data)
        return json_data

details_payloads = {
    'numeroColegiado': '',
    'nombre': 'Jaime',
    'Apellido1': 'Gonzalez',
    'Apellido2': '',
    'idEspecialidad': '',
    'idProvincia': '08',
    'codigoCaptcha': '2edbw',
}

total_good_resps = 0
total_bad_resps = 0
c = 1

while True:
    start = time.time()

    good_resps = 0
    bad_resps = 0

    resps = asyncio.run(get_users_data(details_payloads))

    for resp in resps:
        if resp and 'GONZALEZ' in resp:
            good_resps += 1

        else:
            bad_resps += 1

    end = time.time()

    total_good_resps += good_resps
    total_bad_resps += bad_resps

    print('Good resps:', good_resps, f'(total: {total_good_resps})')
    print('Bad resps:', bad_resps, f'(total: {total_bad_resps})')
    print('Completed Occuration: ' + str(c))
    print('How much resps:', len(resps))
    print(f'Eclipsed time {end - start:.2f} seconds')
    print('-'*30)

    c += 1


'''
Names should be tested:
Format:
FirstName,LastName

Blanca,Moyano
Carmen,Menéndez
Nines,Almazan
Jaime,Campos
María,Fideliz
Laura,Fontirroig
Carmen,Mendoza
Raquel,Mendoza
Ana,Palomo
Obdulia,Serrano
Miguel,Carboni
Arturo,Ruiz
Cristina,Navarro
Domenico,Rosario
Irina,Bobolea
Joan,Bartra
Marcos,Sanchez
Maria,Peña
Maylen,Fariñas
Stefan,Cimbollek
Sara,López

'''
