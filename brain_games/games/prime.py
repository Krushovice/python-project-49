from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def build_game():
    task = randint(2, 99)
    # флаг изначально поднят
    prime = True
    i = 2

    while i <= sqrt(task):

        if task % i == 0:
            prime = False
            break
        i += 1

    if prime:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer, task
