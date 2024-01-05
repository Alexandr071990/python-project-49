from random import randint


QUESTION_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    task = randint(1, 100)
    if check_even(task) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, task


def check_even(task):
    return True if task % 2 == 0 else False
