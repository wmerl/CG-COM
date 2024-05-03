import asyncio
import sys
import time

import aiohttp

from asyncio import Task
from typing import Any
from vars import RequestsVars, Data


temporary_data = []


async def fetch(s, user_data: dict[str: str]) -> Any:

    endpoint_url: str = RequestsVars.ENDPOINT_URL

    cookies: dict[str: str] = {
        'JSESSIONID': RequestsVars.JSESSIONID,
    }

    details_payloads: dict[str: str] = {
        'numeroColegiado': '',
        'nombre': user_data.get('l_name'),
        'Apellido1': user_data.get('f_name'),
        'Apellido2': '',
        'idEspecialidad': '',
        'idProvincia': '08',
        'codigoCaptcha': RequestsVars.CAPTCHA,
    }

    async with s.post(endpoint_url, data=details_payloads, cookies=cookies) as r:
        # print(r.status)

        if r.status == 200 and 'El código de verificación introducido no es correcto' in await r.text():

            sys.exit('invalid captcha code')
            return None

        if r.status == 500:
            r.raise_for_status('JSONSESSION Expires')

        if r.status != 200:
            return None

        return await r.text()


async def fetch_all(s, users_data: dict[str: str]) -> tuple[Any]:

    tasks: list[Task[dict]] = []
    for user_data in users_data:
        task: Task = asyncio.create_task(fetch(s, user_data))
        tasks.append(task)
    res: tuple[Any] = await asyncio.gather(*tasks)
    return res


async def get_users_data(users_data: dict[str: str]) -> tuple[Any]:

    async with aiohttp.ClientSession() as session:
        json_data = await fetch_all(session, users_data)
        return json_data




