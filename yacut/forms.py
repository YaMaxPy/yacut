from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional

from .constants import MAX_LEN_SHORT_URL


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректная ссылка'),
        ],
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, MAX_LEN_SHORT_URL), Optional()],
    )
    submit = SubmitField('Создать')
