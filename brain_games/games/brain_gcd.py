import random

from .meta import GameRound


def compute_gcd(a, b):
    if(b == 0):
        return a
    else:
        return compute_gcd(b, a % b)


def game() -> GameRound:
    a = random.randint(0, 100)
    b = random.randint(0, 100)

    gcd = compute_gcd(a, b)

    return GameRound(question=f'{a} {b}', answer=str(gcd))
