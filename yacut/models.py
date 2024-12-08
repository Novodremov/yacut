from datetime import datetime, timezone
from random import choices
from urllib.parse import urljoin

from flask import url_for

from yacut import db
from .constants import (API_POST_KEYS, API_SHORT_URL_POST_NAME, CHARACTERS,
                        DEFAULT_SHORT_URL_LENGTH, MAX_ORIGINAL_URL_LENGTH,
                        MAX_SHORT_URL_LENGTH, NUMBER_OF_ATTEMPTS,
                        SHORT_URL_EXISTS_ERROR, SHORT_URL_GENERATION_ERROR)
from .error_handlers import MakingUrlException
from .validators import validate_api_custom_id, validate_url_length


class URLMap(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    original = db.Column(
        db.Text(MAX_ORIGINAL_URL_LENGTH),
        nullable=False,
    )
    short = db.Column(
        db.String(MAX_SHORT_URL_LENGTH),
        unique=True,
    )
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now(timezone.utc),
    )

    def to_dict(self):
        base_url = url_for('index_view', _external=True)
        return dict(
            url=self.original,
            short_link=urljoin(base_url, self.short),
        )

    @staticmethod
    def validate_data(data):
        for api_field_name in API_POST_KEYS.values():
            if api_field_name in data:
                validate_url_length(api_field_name, data[api_field_name])
                if api_field_name == API_SHORT_URL_POST_NAME:
                    validate_api_custom_id(data[api_field_name])

    @classmethod
    def get_by_custom_id(cls, custom_id):
        return cls.query.filter_by(short=custom_id).first()

    @classmethod
    def get_unique_short_id(cls):
        '''Генерация короткой ссылки.'''
        for _ in range(NUMBER_OF_ATTEMPTS):
            short_url = ''.join(choices(CHARACTERS,
                                        k=DEFAULT_SHORT_URL_LENGTH))
            if not cls.get_by_custom_id(short_url):
                return short_url
        raise MakingUrlException(SHORT_URL_GENERATION_ERROR)

    @classmethod
    def add_urlmap(cls, original, short, api):
        if cls.get_by_custom_id(short) is not None:
            raise MakingUrlException(SHORT_URL_EXISTS_ERROR)
        if not short:
            short = cls.get_unique_short_id()
        if api:
            cls.validate_data(dict(url=original,
                                   custom_id=short))
        url = cls(
            original=original,
            short=short,
        )
        db.session.add(url)
        db.session.commit()
        return url