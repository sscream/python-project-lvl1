from brain_games.games import brain_gcd
from brain_games.engine import run


def main():
    run(
        round_starter=brain_gcd.prepare_round,
        description=brain_gcd.DESCRIPTION
    )


if __name__ == '__main__':
    main()
