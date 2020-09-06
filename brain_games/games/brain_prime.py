from random import randint
from math import sqrt
from itertools import count, islice

from .meta import GameRound


def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


def game() -> GameRound:
    num = randint(0, 100)

    return GameRound(
        question=str(num),
        answer='yes' if is_prime(num) else 'no'
    )
