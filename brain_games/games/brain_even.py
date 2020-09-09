from random import randint

from brain_games.meta import GameRound


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def prepare_round() -> GameRound:
    number = randint(1, 100)
    answer = 'no' if number % 2 else 'yes'

    return GameRound(question=str(number), answer=answer)
