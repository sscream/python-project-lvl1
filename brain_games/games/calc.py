import operator
import random

from brain_games.meta import GameRound


DESCRIPTION = 'What is the result of the expression?'


def prepare_round() -> GameRound:
    operations = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    ]

    a = random.randint(1, 100)
    b = random.randint(1, 100)

    sign, operation = random.choice(operations)

    answer = operation(a, b)
    question = f'{a} {sign} {b}'

    return GameRound(question=question, answer=str(answer))
