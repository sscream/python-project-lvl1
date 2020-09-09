import random

from brain_games.meta import GameRound


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def compute_gcd(a, b):
    if(b == 0):
        return a
    else:
        return compute_gcd(b, a % b)


def prepare_round() -> GameRound:
    a = random.randint(0, 100)
    b = random.randint(0, 100)

    gcd = compute_gcd(a, b)

    return GameRound(question=f'{a} {b}', answer=str(gcd))
