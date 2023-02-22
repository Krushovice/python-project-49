from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
    NUMBER_1, NUMBER_2 = randint(1, 100), randint(1, 100)
    correct_answer = str(gcd(NUMBER_1, NUMBER_2))
    task = f'{NUMBER_1} {NUMBER_2}'

    return correct_answer, task
