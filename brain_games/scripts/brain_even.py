from brain_games.games.brain_even import ask_question
from brain_games.engine import run


def main():
    run(
        game=ask_question,
        description='Answer "yes" if number even otherwise answer "no".'
    )


if __name__ == '__main__':
    main()
