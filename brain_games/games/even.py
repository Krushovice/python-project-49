from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def build_game():
    task = randint(1, 100)

    def is_prime(build_game):
        if task % 2 == 0:
            correct_answer = 'yes'

        else:
            correct_answer = 'no'

        return correct_answer, task

    return is_prime(build_game)
