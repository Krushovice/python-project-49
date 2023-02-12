import prompt
from brain_progression import build_game, find_number

def start_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    counter = 0
    while counter < 3:
        correct_answer= build_game()
        sequence = find_number()
        user_answer = prompt.string('Your answer:  ')
        if user_answer == correct_answer:
            print('Correct!')
            counter+=1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}\nLet"s try again, {name}!')
            counter = 0

    print(f'Congratulations, {name}! You answered correctly 3 times, well done!')



if __name__ == '__main__':
    main()
