from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    task = randint(1, 100)
    correct_answer = is_even(task)
    return task, correct_answer


def is_even(task):
    return 'no' if task % 2 else 'yes'
