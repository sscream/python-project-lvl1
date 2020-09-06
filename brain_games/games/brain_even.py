from random import randint

from .meta import GameRound


def game() -> GameRound:
    number = randint(1, 100)
    answer = 'no' if number % 2 else 'yes'
    question = f'Question: {number}'

    return GameRound(question=question, answer=answer)
