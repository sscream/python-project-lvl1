from brain_games.games.brain_calc import game
from brain_games.engine import run


def main():
    run(
        game=game,
        description='What is the result of the expression?'
    )


if __name__ == '__main__':
    main()
