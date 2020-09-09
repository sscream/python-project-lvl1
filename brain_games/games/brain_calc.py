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

    operation, function = random.choice(operations)

    answer = function(a, b)
    question = f'{a} {operation} {b}'

    return GameRound(question=question, answer=str(answer))
