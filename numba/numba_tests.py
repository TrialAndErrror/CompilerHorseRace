"""
Testing utilities for Numba
"""
import timeit
from numba import jit
import numpy as np
import random


"""
Numba is a just-in-time compiler for Python that works best on code that uses NumPy arrays and functions, and loops. 
The most common way to use Numba is through its collection of decorators that can be applied to your functions to 
instruct Numba to compile them. When a call is made to a Numba-decorated function it is compiled to machine code 
“just-in-time” for execution and all or part of your code can subsequently run at native machine code speed!
"""


HORSES = [
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
]

WINNERS = {
    'Epona': 0,
    'Torrent': 0,
    'Roach': 0,
    'Shadowmere': 0,
    'Chestnut': 0,
    'Red Hare': 0,
    'Agro': 0,
    'Invincible': 0,
    'Rapidash': 0,
    'Buck': 0,
}


def simulate_race():
    horse_scores = []

    for horse in HORSES:
        horse_scores.append((horse, random.random()))

    horse_scores.sort(key=lambda x: x[1])
    return horse_scores[0][0]


def run_test():
    for num in range(100_000):
        winner = simulate_race()
        WINNERS[winner] += 1


def main():
    run_test()

    print(f'The winner is: {max(WINNERS, key=WINNERS.get)}!')
