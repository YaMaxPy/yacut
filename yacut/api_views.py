import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import REGEXP
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_from_db, get_unique_short_id


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    url = get_from_db(short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' in data:
        custom_id = data.get('custom_id')
        if get_from_db(custom_id).first():
            raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
        if custom_id == '' or custom_id is None:
            data['custom_id'] = get_unique_short_id()
        elif not re.match(REGEXP, custom_id):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
    else:
        data['custom_id'] = get_unique_short_id()
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED
