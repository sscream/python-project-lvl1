from brain_games.games import brain_calc
from brain_games.engine import run


def main():
    run(
        round_starter=brain_calc.prepare_round,
        description=brain_calc.DESCRIPTION
    )


if __name__ == '__main__':
    main()
