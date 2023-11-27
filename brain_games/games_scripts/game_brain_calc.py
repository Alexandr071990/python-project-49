#!/usr/bin/env python3

from operator import add, sub, mul
from random import randint, choice


QUESTION_GAME = 'What is the result of the expression?'
OPERATORS = {'+': add, '-': sub, '*': mul}


def get_number_and_answer():
    first_number, second_number = randint(1, 10), randint(1, 10)
    operator = choice(list(OPERATORS.keys()))
    correct_answer = str(abs(OPERATORS[operator](first_number, second_number)))
    if first_number > second_number:
        task = f'{first_number} {operator} {second_number}'
    elif second_number > first_number:
        task = f'{second_number} {operator} {first_number}'

    return correct_answer, task
