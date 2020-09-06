import typing
from brain_games.cli import get_user_answer, welcome
from brain_games.games.meta import GameRound


def run(
    game: typing.Callable[[], GameRound],
    description: str, rounds: int = 3
):
    print(f'Welcome to the Brain Games!\n{description}')

    round_num = 0

    name = welcome()

    while round_num < rounds:
        game_round = game()

        print(game_round.question)

        user_answer = get_user_answer()

        if user_answer == game_round.answer:
            print('Correct!')
            round_num += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{game_round.answer}'. "
                f"Let's try again, {name}!"
            )
            return

    print(f'Congratulations! {name}')
