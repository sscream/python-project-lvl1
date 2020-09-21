from random import randint

from brain_games.meta import GameRound


DESCRIPTION = 'What number is missing in the progression?'


def prepare_round() -> GameRound:
    length = 10

    start = randint(0, 100)
    step = randint(1, 10)
    missing_element_index = randint(0, length - 1)

    progression = [
        str(start + i * step)
        for i in range(length)
    ]

    answer = progression[missing_element_index]

    question = ' '.join([
        number if i != missing_element_index else '..'
        for i, number in enumerate(progression)
    ])

    return GameRound(
        question=question,
        answer=answer
    )
