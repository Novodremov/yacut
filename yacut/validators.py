import re

from .constants import (API_SHORT_URL_POST_NAME, NAME_ERROR_MESSAGES,
                        VALID_LENGTHS)
from .error_handlers import InvalidAPIUsage


def checking_name(value):
    if not re.match("^[a-zA-Z0-9]*$", value):
        raise InvalidAPIUsage(NAME_ERROR_MESSAGES[API_SHORT_URL_POST_NAME])


def validate_custom_id(form, field):
    checking_name(field.data)


def validate_url_length(field, value):
    if not (VALID_LENGTHS[field][0] <= len(value) <= VALID_LENGTHS[field][1]):
        raise InvalidAPIUsage(
            NAME_ERROR_MESSAGES[field])
