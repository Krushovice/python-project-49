import prompt
from random import randint, choice


def find_number():
    sequence = []
    number, step = randint(0, 50), randint(0, 50)
    for i in range(10):
        number+=step
        sequence.append(number)
    return sequence

def build_game():
    print('What number is missing in the progression?')
    sequence = find_number()
    random_index = randint(0,9)
    correct_answer = str(sequence[random_index])
    sequence[random_index] = '..'
    print('Question: ', end='')
    print(*sequence)

    return correct_answer
