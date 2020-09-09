from brain_games.games import brain_prime
from brain_games.engine import run


def main():
    run(
        round_starter=brain_prime.prepare_round,
        description=brain_prime.DESCRIPTION
    )


if __name__ == '__main__':
    main()
