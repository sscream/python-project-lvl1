import operator
import random

from .meta import GameRound


def game() -> GameRound:
    operators = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    )

    a = random.randint(1, 100)
    b = random.randint(1, 100)

    op, fn = random.choice(operators)

    answer = fn(a, b)

    return GameRound(question=f'{a} {op} {b}', answer=str(answer))
