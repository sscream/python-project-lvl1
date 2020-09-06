from brain_games.games.brain_progression import game
from brain_games.engine import run


def main():
    run(
        game=game,
        description='What number is missing in the progression?'
    )


if __name__ == '__main__':
    main()
