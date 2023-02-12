import prompt
from random import randint, choice


def find_number():
    #Расчитываем арифметическую последовательсть
    task = []
    number, step = randint(0, 50), randint(0, 50)
    for i in range(10):
        number+=step
        task.append(number)
    return task

def build_game():
    #Основная функция задачи
    task = find_number()
    random_index = randint(0,9)
    correct_answer = str(task[random_index])
    task[random_index] = '..'
    question = f'What number is missing in the progression?\nQestion: {task}'
    return correct_answer, question

    correct_answer = build_game()
    question = build_game()
