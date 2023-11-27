#!/usr/bin/env python3

from random import randint

QUESTION_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(task):
    k = 0
    for i in range(2, (task // 2) + 1):
        if task % i == 0:
            k = + 1
    if (k <= 0):
        return True
    else:
        return False


def get_number_and_answer():
    task = randint(1, 50)
    if is_prime(task) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, task
