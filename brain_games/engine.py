"""
brain games engine

pass game attribute as a game module with 'DESCRIPTION' property
and 'prepare_round' method to run game
"""

import typing
import prompt


def run(game: typing.Optional = None, rounds_total: int = 3):
    print('Welcome to the Brain Games!')

    if game is not None:
        print(game.DESCRIPTION)

    name = prompt.string('May I have your name? ')
    print(f'Hello {name}')

    if game is not None:
        current_round_num = 0

        while current_round_num < rounds_total:
            question, answer = game.prepare_round()

            print(f'Question: {question}')

            user_answer = prompt.string("Your answer: ")

            if user_answer == answer:
                print('Correct!')
                current_round_num += 1
            else:
                print(
                    f"'{user_answer}' is wrong answer ;(. "
                    f"Correct answer was '{answer}'.\n"
                    f"Let's try again, {name}!"
                )
                return

        print(f'Congratulations! {name}')
