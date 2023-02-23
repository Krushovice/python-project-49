from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    task = randint(2, 99)
    correct_answer = is_prime(task)
    return correct_answer, task


def is_prime(task):
    i = 2
    while i <= sqrt(task):
        if task % i == 0:
            return 'no'
        i += 1
    return 'yes'
