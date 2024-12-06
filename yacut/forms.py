from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL

from .constants import (MIN_ORIGINAL_URL_LENGTH, MIN_SHORT_URL_LENGTH,
                        MAX_ORIGINAL_URL_LENGTH, MAX_SHORT_URL_LENGTH)
from .validators import validate_custom_id


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите ссылку, которую хотите сократить',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_ORIGINAL_URL_LENGTH, MAX_ORIGINAL_URL_LENGTH),
                    URL(message='Введите корректную ссылку')]
    )
    custom_id = StringField(
        'Введите ваш вариант короткой ссылки',
        validators=[Length(MIN_SHORT_URL_LENGTH, MAX_SHORT_URL_LENGTH),
                    Optional(),
                    validate_custom_id]
    )
    submit = SubmitField('Создать')
