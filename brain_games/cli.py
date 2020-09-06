import prompt


def welcome() -> str:
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}')

    return name


def get_user_answer():
    return prompt.string("Your answer: ")
