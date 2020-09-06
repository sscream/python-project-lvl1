from random import randint

from .meta import GameRound


def game() -> GameRound:
    length = 10

    start = randint(0, 100)
    step = randint(1, 10)
    missing_index = randint(0, length - 1)

    progression = []

    for i in range(length):
        num = str(start + i * step)

        if i == missing_index:
            progression.append('..')
            answer = num
        else:
            progression.append(num)

    return GameRound(
        question=' '.join(progression),
        answer=answer
    )
