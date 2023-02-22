from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    task = randint(1, 100)

    def is_even(build_game):
        if task % 2 == 0:
            correct_answer = 'yes'

        else:
            correct_answer = 'no'

        return correct_answer, task

    return is_even(make_question)
