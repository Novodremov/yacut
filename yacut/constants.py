from string import ascii_letters, digits

MAIN_PAGE_TEMPLATE = 'index.html'

CHARACTERS = ascii_letters + digits
NUMBER_OF_CHARS_FOR_SHORT_URL = 6

REGEX_PATTERN = '^[a-zA-Z0-9]*$'
NUMBER_OF_ATTEMPTS = 10000

API_ORIGINAL_URL_POST_NAME = 'url'
API_SHORT_URL_POST_NAME = 'custom_id'

API_POST_KEYS = {'original': API_ORIGINAL_URL_POST_NAME,
                 'short': API_SHORT_URL_POST_NAME}

MIN_ORIGINAL_URL_LENGTH = 1
MAX_ORIGINAL_URL_LENGTH = 2000

DEFAULT_SHORT_URL_LENGTH = 6
MIN_SHORT_URL_LENGTH = 1
MAX_SHORT_URL_LENGTH = 16

VALID_LENGTHS = {API_ORIGINAL_URL_POST_NAME: (MIN_ORIGINAL_URL_LENGTH,
                                              MAX_ORIGINAL_URL_LENGTH),
                 API_SHORT_URL_POST_NAME: (MIN_SHORT_URL_LENGTH,
                                           MAX_SHORT_URL_LENGTH)}

NAME_ERROR_MESSAGES = {API_ORIGINAL_URL_POST_NAME:
                       'Недопустимая длина ссылки',
                       API_SHORT_URL_POST_NAME:
                       'Указано недопустимое имя для короткой ссылки'}
SHORT_URL_EXISTS_ERROR = 'Предложенный вариант короткой ссылки уже существует.'
SHORT_URL_GENERATION_ERROR = '''Генерация ссылки не удалась. Попробуйте снова
                                или введите свой вариант короткой ссылки.'''
