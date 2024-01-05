from random import randint
from math import gcd

QUESTION_GAME = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num_1, num_2 = randint(1, 20), randint(1, 20)
    correct_answer = str(gcd(num_1, num_2))
    task = f'{num_1} {num_2}'
    return correct_answer, task
