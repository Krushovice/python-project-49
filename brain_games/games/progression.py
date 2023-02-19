from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    # Расчитываем арифметическую последовательность
    task = []
    initial_number, difference = randint(0, 50), randint(0, 50)
    length = 10
    for index in range(length):
        initial_number += difference
        task.append(initial_number)

    random_index = randint(0, 9)
    correct_answer = str(task[random_index])
    return task, correct_answer, random_index


def build_game():
    # Основная функция задачи
    task, correct_answer, random_index = make_progression()
    task[random_index] = '..'
    task = ' '.join(str(i) for i in task)
    return correct_answer, task
