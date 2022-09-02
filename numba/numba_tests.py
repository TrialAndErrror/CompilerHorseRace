"""
Testing utilities for Numba
"""
import time
from numba import jit
import json
import numpy as np
from scipy import stats
import statistics

"""
Numba is a just-in-time compiler for Python that works best on code that uses NumPy arrays and functions, and loops. 
The most common way to use Numba is through its collection of decorators that can be applied to your functions to 
instruct Numba to compile them. When a call is made to a Numba-decorated function it is compiled to machine code 
“just-in-time” for execution and all or part of your code can subsequently run at native machine code speed!
"""


HORSES = np.array((
    'Epona',
    'Torrent',
    'Roach',
    'Shadowmere',
    'Chestnut',
    'Red Hare',
    'Agro',
    'Invincible',
    'Rapidash',
    'Buck'
))


def numpy_race():
    results = np.random.rand(100_000, 10)
    winner_ids = np.argmax(results,axis=1)
    champion_id = stats.mode(winner_ids)[0]
    champion = HORSES[champion_id]
    return champion


def run_with_timer(num):
    print(f'Loop Num {num}')
    start = time.perf_counter()
    champion = numpy_race()
    stop = time.perf_counter()
    print(f'The champion is: {champion}')
    return stop - start


@jit(nopython=True)
def run_compiled_with_timer(num):
    print(f'Loop Num {num}')
    results = np.random.rand(100_000, 10)
    winner_ids = np.argmax(results, axis=1)

    freq = {}
    for i in winner_ids:
        freq.setdefault(i, 0)
        freq[i] += 1

    hf = max(freq.values())

    hflst = []

    for i, j in freq.items():
        if j == hf:
            hflst.append(i)

    champion_id = hflst[0]

    champion = HORSES[champion_id]

    print(f'The champion is: {champion}')


def mode(lst):
    freq = {}
    for i in lst:
        freq.setdefault(i, 0)
        freq[i] += 1

    hf = max(freq.values())

    hflst = []

    for i, j in freq.items():
        if j == hf:
            hflst.append(i)

    return hflst


def run_with_numba():
    start: float = time.perf_counter()

    times = [
        run_compiled_with_timer(num)
        for num in range(100)
    ]
    stop: float = time.perf_counter()

    print(f'Fastest: {min(times)}')
    print(f'Slowest: {max(times)}')
    print('All Times:')
    print(sorted(times))

    results = {
        'Fastest': min(times),
        "Slowest": max(times),
        "Times": sorted(times)

    }

    with open('numba_results.json', 'w+') as file:
        json.dump(results, file, indent=2)


def run_standard_numpy():
    times = [run_with_timer(num)
             for num in range(100)]

    print(f'Fastest: {min(times)}')
    print(f'Slowest: {max(times)}')
    print('All Times:')
    print(sorted(times))

    results = {
        'Fastest': min(times),
        "Slowest": max(times),
        "Times": sorted(times)

    }

    with open('plain_results.json', 'w+') as file:
        json.dump(results, file, indent=2)


if __name__ == '__main__':
    run_with_numba()
