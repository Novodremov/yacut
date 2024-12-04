from random import choices
from string import ascii_letters, digits

from .constants import DEFAULT_SHORT_URL_LENGTH
from .models import URLMap


def get_unique_short_id():
    '''Генерация короткой ссылки.'''
    characters = ascii_letters + digits
    while True:
        short_url = ''.join(choices(characters,
                                    k=DEFAULT_SHORT_URL_LENGTH))
        if not URLMap.query.filter_by(short=short_url).first():
            return short_url
