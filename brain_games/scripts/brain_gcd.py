from brain_games.games.brain_gcd import game
from brain_games.engine import run


def main():
    run(
        game=game,
        description='Find the greatest common divisor of given numbers.'
    )


if __name__ == '__main__':
    main()
