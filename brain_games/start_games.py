import prompt
ROUNDS = 3


def start_or_end_games(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION_GAME)
    for _ in range(ROUNDS):
        random, answer = game.get_number_and_answer()
        print(f'Question: {random}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == answer:
            print(f'Correct!')
        if your_answer != answer:
            print(f"{your_answer} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')
