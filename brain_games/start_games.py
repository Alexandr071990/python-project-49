import prompt
ROUNDS = 3


def start_or_end_games(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION_GAME)
    for _ in range(ROUNDS):
        correct_answer, task = game.get_number_and_answer()
        print(f'Question: {task}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == correct_answer:
            print('Correct!')
        if your_answer != correct_answer:
            print(f"{your_answer} is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
