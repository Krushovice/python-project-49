from random import randint
from math import gcd


QUESTION = 'Find the greatest common divisor of given numbers.'


def build_game():
    # Задаем 2 числа и находим их делители
    num1, num2 = randint(1, 100), randint(1, 100)
    correct_answer = str(gcd(num1, num2))
    task = f'{num1} {num2}'

    return correct_answer, task
