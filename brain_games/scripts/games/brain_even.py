import prompt
from random import randint
from brain_games.scripts.cli import welcome_user, name

def parity_check():

    counter = 0
    while counter < 3:
        number = randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ').lower()

        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('Current!')
            counter += 1

        elif number % 2 == 0 and answer == 'no':
            print(f'Wrong answer! Correct answer is "yes".\nBetter luck next time\nLet"s try again, {name}!')

        elif number % 2 != 0 and answer == 'yes':
            print(f'Wrong answer! Correct answer is "no".\nBetter luck next time\nLet"s try again, {name}!')

    print(f'Congratulations, {name}!')



def main():
    welcome_user()
    parity_check()


if __name__ == '__main__':
    main()
