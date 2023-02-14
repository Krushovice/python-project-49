from random import randint, choice

QUESTION = 'What is the result of the expression?'


def build_game():
    '''Задаем операторы по умолчанию,находим
       2 числа и выбираем случайный оператор из списка
    '''
    operators = ['+', '-', '*']

    num1, num2 = randint(1, 100), randint(1, 100)
    operator = choice(operators)

    if num1 < num2:
        if operator == '-':
            result = num2 - num1
        elif operator == '+':
            result = num1 + num2
        else:
            result = num1 * num2

        task = f'{num2} {operator} {num1}'

    if num1 > num2:
        if operator == '-':
            result = num1 - num2
        elif operator == '+':
            result = num1 + num2
        else:
            result = num1 * num2

        task = f'{num1} {operator} {num2}'

    correct_answer = str(result)

    return correct_answer, task
