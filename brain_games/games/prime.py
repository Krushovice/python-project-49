from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    task = randint(2, 99)
    i = 2
    while i <= sqrt(task):

        if task % i == 0:
            correct_answer = 'no'
            return

        i += 1
    correct_answer = 'yes'
    return task, correct_answer
