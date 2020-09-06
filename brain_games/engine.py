import typing
from brain_games.cli import get_user_answer, welcome


def run(
    game: typing.Callable[[], typing.Tuple[str, str]],
    description: str, rounds: int = 3
):
    print(f'Welcome to the Brain Games!\n{description}')

    round_num = 0

    name = welcome()

    while round_num < rounds:
        question, correct_answer = game()

        print(question)

        user_answer = get_user_answer()

        if user_answer == correct_answer:
            print('Correct!')
            round_num += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'. "
                f"Let's try again, {name}!"
            )
            return

    print(f'Congratulations! {name}')
