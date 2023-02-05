import prompt
from random import randint
from brain_games.scripts.cli import welcome_user, name

def find_divisor():
    counter = 0
    print('Find the greatest common divisor of given numbers.')
    while counter < 3:
        num1, num2 = randint(1, 100), randint(1, 100)
        first_divisors = []
        second_divisors = []
        i = 1
        while i < num1:
            if num1 % i == 0:
                first_divisors.append(i)
            i+=1

        x = 1
        while x < num2:
            if num2 % x == 0:
                second_divisors.append(x)
            x += 1

        result = [x for x in first_divisors if x in second_divisors]
        correct_answer = str(max(result))

        question = f'{num1} {num2}'
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if correct_answer == user_answer:
            print('Coorect!')
            counter+=1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet"s try again, {name}')
            counter = 0


    print(f'Congratulations, {name}! You answered correctly 3 times, well done!')


def main():
    welcome_user()
    find_divisor()


if __name__ == '__main__':
    main()
