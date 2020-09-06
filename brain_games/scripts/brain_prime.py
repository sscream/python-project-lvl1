from brain_games.games.brain_prime import game
from brain_games.engine import run


def main():
    run(
        game=game,
        description=(
            'Answer "yes" if given number is prime. Otherwise answer "no".'
        )
    )


if __name__ == '__main__':
    main()
