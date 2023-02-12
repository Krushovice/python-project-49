import prompt
from random import randint, choice


def prime_or_not():
    counter = 0
    while counter < 3:
        number = randint(2, 99)

        def check_number(number):

            for i in range(2, (number//2)+1):
                if number % i == 0:
                    return False
            return True
        if check_number(number) == False:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ').lower()

        if user_answer == correct_answer:
            print('Correct!')
            counter+=1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet"s try again, {name}')
            counter = 0

    print(f'Congratulations, {name}! You answered correctly 3 times, well done!')


def main():
    welcome_user()
    prime_or_not()



if __name__ == '__main__':
    main()
