import prompt
from random import randint, choice
from brain_games.scripts.cli import welcome_user, name


operators = ['+', '-', '*']
def calculate():
    counter = 0

    while counter < 3:
        num1, num2 = randint(1, 100), randint(1, 100)
        operator = choice(operators)

        if num1 < num2:
            if operator == '-':
                result = num2 - num1
            elif operator == '+':
                result = num1 + num2
            else:
                result = num1 * num2

            quest = f'{num2} {operator} {num1}'

        if num1 > num2:
            if operator == '-':
                result = num1 - num2
            elif operator == '+':
                result = num1 + num2
            else:
                result = num1 * num2

            quest = f'{num1} {operator} {num2}'


        print(f'What is the result of the expression?\nQestion: {quest}')
        correct_answer = str(result)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print(f'Current!')
            counter += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet"s try again, Sam!')
            counter = 0

    print(f'Congratulations, {name}! You answered correctly 3 times, well done!')



def main():
    welcome_user()
    calculate()


if __name__ == '__main__':
    main()
