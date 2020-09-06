from random import randint


def ask_question():
    number = randint(1, 100)
    answer = 'no' if number % 2 else 'yes'
    question = f'Question: {number}'

    return question, answer
