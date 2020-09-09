from brain_games.games import brain_even
from brain_games.engine import run


def main():
    run(
        round_starter=brain_even.prepare_round,
        description=brain_even.DESCRIPTION
    )


if __name__ == '__main__':
    main()
