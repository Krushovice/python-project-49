from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    correct_answer = str(gcd(number_1, number_2))
    task = f'{number_1} {number_2}'

    return correct_answer, task
