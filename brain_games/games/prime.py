from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    task = randint(2, 99)
    flag = is_prime(task)
    if flag is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, task


def is_prime(task):
    i = 2
    while i <= sqrt(task):
        if task % i == 0:
            return False
        i += 1
    return True
