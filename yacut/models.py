from datetime import datetime
from urllib.parse import urljoin

from flask import request

from . import db
from .constants import FIELD_NAMES


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=urljoin(request.url_root, self.short),
        )

    def from_dict(self, data):
        for field_db, field_request in FIELD_NAMES.items():
            if field_request in data:
                setattr(self, field_db, data[field_request])
