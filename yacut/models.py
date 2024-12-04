from datetime import datetime, timezone
from urllib.parse import urljoin

from flask import url_for

from yacut import db
from .constants import (API_POST_KEYS, API_SHORT_URL_POST_NAME,
                        MAX_ORIGINAL_URL_LENGTH, MAX_SHORT_URL_LENGTH)
from .validators import checking_name, validate_url_length


class URLMap(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    original = db.Column(
        db.String(MAX_ORIGINAL_URL_LENGTH),
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

    def from_dict(self, data):
        for model_field_name, api_field_name in API_POST_KEYS.items():
            if api_field_name in data:
                validate_url_length(api_field_name, data[api_field_name])
                if api_field_name == API_SHORT_URL_POST_NAME:
                    checking_name(data[api_field_name])
                setattr(self, model_field_name, data[api_field_name])
