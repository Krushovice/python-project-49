import prompt
from random import randint
from brain_games.scripts.cli import welcome_user


def parity_check():
    counter = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while counter < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ').lower()

        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('Current!')
            counter += 1

        elif (number % 2 == 0 and answer == 'no') or (number % 2 != 0 and answer == 'yes') :
            print(f'Wrong answer! Correct answer is "yes".\nBetter luck next time\nLet"s try again, {name}!')
            counter = 0


    print(f'Congratulations, {name}!')



def main():

    welcome_user()
    parity_check()


if __name__ == '__main__':
    main()
