from random import randint
from cli import welcome_user, name

def parity_check():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input()
        print(f'Your answer: {answer}')

        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('Current!')
            counter += 1

        else:
            print(f'''Wrong answer! Better luck next time
Let's try again, {name}!''')


    print(f'Congratulations, {name}!')

parity_check()


def main():
    parity_check()


if __name__ == '__main__':
    main()
