from random import randint


QUESTION = 'Find the greatest common divisor of given numbers.'


def build_game():
    # Задаем 2 числа и находим их делители
    num1, num2 = randint(1, 100), randint(1, 100)
    first_divisors = []
    second_divisors = []
    i = 1
    while i < num1:
        if num1 % i == 0:
            first_divisors.append(i)
        i += 1

    x = 1
    while x < num2:
        if num2 % x == 0:
            second_divisors.append(x)
        x += 1

    result = [x for x in first_divisors if x in second_divisors]
    correct_answer = str(max(result))

    task = f'{num1} {num2}'

    return correct_answer, task
