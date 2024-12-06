import re

from wtforms import ValidationError

from .constants import (API_SHORT_URL_POST_NAME, NAME_ERROR_MESSAGES,
                        REGEX_PATTERN, VALID_LENGTHS)
from .error_handlers import InvalidAPIUsage


def validate_api_custom_id(value):
    if not re.match(REGEX_PATTERN, value):
        raise InvalidAPIUsage(NAME_ERROR_MESSAGES[API_SHORT_URL_POST_NAME])


def validate_custom_id(form, field):
    if not re.match(REGEX_PATTERN, field.data):
        raise ValidationError(NAME_ERROR_MESSAGES[API_SHORT_URL_POST_NAME])


def validate_url_length(field, value):
    if not (VALID_LENGTHS[field][0] <= len(value) <= VALID_LENGTHS[field][1]):
        raise InvalidAPIUsage(
            NAME_ERROR_MESSAGES[field])
