import typing
import prompt

from brain_games.meta import GameRound


def run(
    round_starter: typing.Optional[typing.Callable[[], GameRound]] = None,
    description: str = '', rounds_total: int = 3
):
    print('Welcome to the Brain Games!')
    print(description)

    name = prompt.string('May I have your name? ')
    print(f'Hello {name}')

    if round_starter is not None:
        current_round_num = 0

        while current_round_num < rounds_total:
            question, answer = round_starter()

            print(f'Question: {question}')

            user_answer = prompt.string("Your answer: ")

            if user_answer == answer:
                print('Correct!')
                current_round_num += 1
            else:
                print(
                    f"'{user_answer}' is wrong answer ;(. "
                    f"Correct answer was '{answer}'. "
                    f"Let's try again, {name}!"
                )
                return

        print(f'Congratulations! {name}')
