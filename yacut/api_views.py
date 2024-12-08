from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage, MakingUrlException
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    if not request.data or not (data := request.get_json()):
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    short = data.get('custom_id')
    try:
        url = URLMap.add_urlmap(data['url'], short, api=True)
        return jsonify(url.to_dict()), HTTPStatus.CREATED
    except MakingUrlException as error:
        raise InvalidAPIUsage(str(error))


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_link(short_id):
    url = URLMap.get_by_custom_id(short_id)
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK
