from random import randint, choice
import prompt


operators = ['+', '-', '*']
def calculate():
    counter = 0

    while counter < 3:
        num1, num2 = randint(1, 250), randint(1, 250)
        operator = choice(operators)

        if num1 > num2:
            result = f'{num1}{operator}{num2}'
        else:
            result = f'{num2}{operator}{num1}'

        print(f'What is the result of the expression?\nQestion: {result}')
        correct_answer = result
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print(f'Current!')
            counter += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet"s try again, Sam!')
            counter = 0


calculate()
