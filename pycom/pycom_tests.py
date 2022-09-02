"""
Testing utilities for PyCom
"""
import random

"""
Supported Features

    All 'turing complete' features of Python: if, else, for, while, etc.
    f'' strings
    Some in built functions
    Some math library functions
    List comprehensions
    Python-style arbitarily large intergers

Not supported yet

    Pythonic ways of writing certain blocks (one line if...else, etc.)
    Multi-line string literals
    A lot of libraries included in stdlib
    Classes
    The throw and finally keywords
    Heterogeneous lists; lists with more than one data type in them
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
