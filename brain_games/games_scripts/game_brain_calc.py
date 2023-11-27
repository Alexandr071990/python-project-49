#!/usr/bin/env python3

import random
from random import randint


QUESTION_GAME = 'What is the result of the expression?'


def calculator(first_number, operator, second_number):
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    elif operator == '*':
        correct_answer = first_number * second_number
    return correct_answer


def get_number_and_answer():
    first_number, second_number = randint(1, 10), randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    task = f'{first_number} {operator} {second_number}'
    correct_answer = str(calculator(first_number, operator, second_number))

    return correct_answer, task
