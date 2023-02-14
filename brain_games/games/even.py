from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def build_game():
    # Находим рандомное число и проверяем на чётность
    task = randint(1, 100)
    if task % 2 == 0:
        correct_answer = 'yes'

    else:
        correct_answer = 'no'

    return correct_answer, task
