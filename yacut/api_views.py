from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    if not request.data or not (data := request.get_json()):
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    short = data['custom_id'] if 'custom_id' in data else None
    return URLMap.add_urlmap(data['url'], short, api=True)


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_link(short_id):
    url = URLMap.get_by_custom_id(short_id)
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK
