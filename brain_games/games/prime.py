import prompt
from random import randint, choice
from math import sqrt

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def build_game():
    #Находим рандомное число
    task = randint(2, 99)
    prime =True   # флаг изначально поднят
    i = 2
    while i <= sqrt(task):
        #Запускаем проверку делителей квадрата числа, начиная с 2
        if task % i == 0:
            prime = False
            break
        i += 1

    if prime:
    #Если флаг остался поднят, то число простое
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer, task
