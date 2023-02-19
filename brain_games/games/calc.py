from operator import add, sub, mul
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def build_game():

    OPERATORS = {
        '+': add,
        '-': sub,
        '*': mul
    }

    FIRST_NUMBER, SECORD_NUMBER = randint(1, 50), randint(1, 50)
    operator = choice(list(OPERATORS.keys()))
    correct_answer = str(abs(OPERATORS[operator](FIRST_NUMBER, SECORD_NUMBER)))
    if FIRST_NUMBER > SECORD_NUMBER:
        task = f'{FIRST_NUMBER} {operator} {SECORD_NUMBER}'
    elif SECORD_NUMBER > FIRST_NUMBER:
        task = f'{SECORD_NUMBER} {operator} {FIRST_NUMBER}'

    return correct_answer, task
