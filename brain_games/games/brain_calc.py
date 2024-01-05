import random
from operator import add, sub, mul
from random import randint


QUESTION_GAME = 'What is the result of the expression?'
OPERATOR = {'+': add, '-': sub, '*': mul}


def get_question_and_answer():
    first_number, second_number = randint(1, 10), randint(1, 10)
    operator = random.choice(list(OPERATOR.keys()))
    task = f'{first_number} {operator} {second_number}'
    correct_answer = str(OPERATOR[operator](first_number, second_number))

    return correct_answer, task
