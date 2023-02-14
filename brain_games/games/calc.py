from random import randint, choice
from operator import add, sub, mul

QUESTION = 'What is the result of the expression?'


def build_game():
    '''Задаем операторы по умолчанию,находим
       2 числа и выбираем случайный оператор из списка
    '''
    SYMBOL, OPERATION = choice((
        ('+', add),
        ('-', sub),
        ('*', mul),))

    num1, num2 = randint(1, 100), randint(1, 100)

    correct_answer = abs(OPERATION(num1, num2))
    if num1 > num2:
        task = f'{num1} {OPERATION} {num2}'
    elif num2 > num1:
        task = f'{num2} {OPERATION} {num1}'

    return correct_answer, task
