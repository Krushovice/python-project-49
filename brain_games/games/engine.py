import prompt


def start_game(game):
    # Приветсвуем игрока
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION)
    counter = 0
    while counter < 3:
        # Выводим вопрос игры и задаем счетчик для прохода по циклу
        correct_answer, task = game.build_game()
        print(f'Qestion: {task}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            # Проверяем ответ пользователя
            print('Correct!')
            counter += 1
        else:
            print(f'''{user_answer} is wrong answer ;(.
            \nCorrect answer was {correct_answer}
            \nLet"s try again, {name}!''')
            counter = 0

    print(f'''Congratulations, {name}!
            You answered correctly 3 times!
          ''')
