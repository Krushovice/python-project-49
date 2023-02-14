import prompt


def start_game(game):
    # Приветсвуем игрока
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION)
    counter = 0
    is_won = True
    while counter < 3:
        # Выводим вопрос игры и задаем счетчик для прохода по циклу
        correct_answer, task = game.build_game()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            # Проверяем ответ пользователя
            print('Correct!')
            counter += 1

        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            is_won = False
            break

    if is_won:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
