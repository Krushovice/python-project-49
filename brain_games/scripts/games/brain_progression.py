import prompt
from random import randint, choice
from brain_games.scripts.cli import welcome_user

def find_number():
    print('What number is missing in the progression?')
    counter = 0

    while counter < 3:
        sequence = []
        number, step = randint(0, 50), randint(0, 50)
        for i in range(10):
            number+=step
            sequence.append(number)

        random_index = randint(0,9)
        correct_answer = str(sequence[random_index])
        sequence[random_index] = '..'

        print('Question: ', end='')
        print(*sequence)
        user_answer = prompt.string('Your answer:  ')

        if user_answer == correct_answer:
            print('Correct!')
            counter+=1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}\nLet"s try again, {name}!')
            counter = 0

    print(f'Congratulations, {name}! You answered correctly 3 times, well done!')


def main():
    welcome_user()
    find_number()


if __name__ == '__main__':
    main()
