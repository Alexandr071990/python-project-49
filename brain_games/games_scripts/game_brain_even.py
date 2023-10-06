#!/usr/bin/env python3

from random import randint


QUESTION_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_even(x):
    if int(x % 2) == 0:
        answer = True
    elif int(x % 2) != 0:
        answer = False
    return answer

def get_number_and_answer():
    random = randint(1, 100)
    if check_even(random) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return random, answer
