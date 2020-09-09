from brain_games.games import brain_progression
from brain_games.engine import run


def main():
    run(
        round_starter=brain_progression.prepare_round,
        description=brain_progression.DESCRIPTION
    )


if __name__ == '__main__':
    main()
