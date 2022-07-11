from random import choice
from string import ascii_letters, digits

SIZE = 7  # > 78 млрд уникальных ссылок
AVAILABLE_CHARS = ascii_letters + digits


def gen_link(ascii_uppercase=AVAILABLE_CHARS, size=SIZE):
    return ''.join(choice(ascii_uppercase) for _ in range(size))
