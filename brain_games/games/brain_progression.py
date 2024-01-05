from random import randint

QUESTION_GAME = 'What number is missing in the progression?'


def get_progression():
    task = []
    start, stop = randint(1, 10), randint(1, 10)
    lenght = 10
    for i in range(lenght):
        start = start + stop
        task.append(start)
    return task


def get_question_and_answer():
    task = get_progression()
    index_to_replace = randint(0, 9)
    correct_answer = str(task[index_to_replace])
    task[index_to_replace] = '..'
    task = ' '.join(str(i) for i in task)
    return correct_answer, task
