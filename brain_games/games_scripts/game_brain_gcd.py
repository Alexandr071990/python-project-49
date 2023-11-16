#!/usr/bin/env python3

from random import randint
from math import gcd

QUESTION_GAME = 'Find the greatest common divisor of given numbers.'


def finde_gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def get_number_and_answer():
    num_1, num_2 = randint(1, 20), randint(1, 20)
    correct_answer = str(finde_gcd(num_1, num_2))
    task = f'{num_1} {num_2}'
    return correct_answer, task
