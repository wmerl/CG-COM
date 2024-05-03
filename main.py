import asyncio
import time

from helpers import get_users_data
from vars import Data

total_good_resps = 0
total_bad_resps = 0
c = 1

persons = Data.PERSONS

subarrays = [persons[i:i+10] for i in range(0, len(persons), 10)]

for ten_persons in subarrays:
    start = time.time()

    good_resps = 0
    bad_resps = 0
    # print('ten_persons', ten_persons)
    resps = asyncio.run(get_users_data(ten_persons))

    for resp in resps:
        if resp and 'No hay datos' not in resp:
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