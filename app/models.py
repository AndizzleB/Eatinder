""" App Models """

import os, hashlib

from flask_admin.contrib.sqla import ModelView
from flask_admin.model import BaseModelView
from flask_admin.form import ImageUploadField
from werkzeug import secure_filename
from urllib.parse import urlencode

from . import db
from .config import Config

import enum, datetime
from sqlalchemy.types import Enum

import geojson

LABEL_NAMES = (
    "Food Preferences",
    "Dietary Requirements",
    "Environmental Impact",
)

class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), nullable=False)
    of_type = db.Column(Enum(*LABEL_NAMES, name="Type"), nullable=False)
    icon = db.Column(db.String(256))
    def __repr__(self):
        return self.name
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon,
            'of_type': self.of_type
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(128))

    # password = db.Column(db.String(64))
    # Flask-Login integration
    # def is_authenticated(self): return True
    # def is_active(self):        return True
    # def is_anonymous(self):     return False
    # def get_id(self):           return self.id

    def __unicode__(self):
        return self.username
    def __repr__(self):
        return self.username
    def gravatar(self):
        gr_size = 80
        if self.email == "": return "/img/usericon.png"
        email = self.email.lower().encode('utf-8')
        gravatar_url = "https://www.gravatar.com/avatar/"
        gravatar_url += hashlib.md5(email).hexdigest() + "?"
        gravatar_url += urlencode({'s':str(gr_size)})
        return gravatar_url
    def dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'gravatar': self.gravatar(),
        }
    # def get_geojson(self):
        # features = [{'type': 'Feature',
        #     'geometry': to_shape(m.location),
        #     'properties': {'date': m.created}
        # } for m in self.meals ]
        # return geojson.dumps(
        #     {'type': 'FeatureCollection', 'features': features}
        # )

class UserView(ModelView):
    column_list = ('id', 'username')


label_meal = db.Table(
    'label_meal',
    db.Column('label_id', db.Integer(), db.ForeignKey('label.id')),
    db.Column('meal_id', db.Integer(), db.ForeignKey('meal.id'))
)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    photo = db.Column(db.String(256))
    created = db.Column(db.DateTime(), default=datetime.datetime.now())
    location_lat = db.Column(db.Float)
    location_lng = db.Column(db.Float)
    recipe_url = db.Column(db.String(2048))

    labels = db.relationship('Label', secondary=label_meal,
        backref=db.backref('meals', lazy='dynamic'))

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User,
        backref=db.backref('meal', cascade="all, delete-orphan", single_parent=True))

    def __repr__(self):
        return str(self.created)
    def thumb(self):
        if not self.photo: return None
        name, _ = os.path.splitext(self.photo)
        return '/photos/' + secure_filename('%s_thumb.jpg' % name)
    def dict(self):
        return {
            'id': self.id,
            'created': self.created.strftime("%Y-%d-%m"),
            'photo': self.photo,
            'thumbnail': self.thumb(),
            'recipe': self.recipe_url,
            'user': self.user.dict(),
            'labels': [ l.dict() for l in self.labels ],
        }

class MealView(ModelView):
    column_list = ('created', 'labels', 'user')
    form_extra_fields = {
        'photo': ImageUploadField('Photo',
            base_path=Config.PHOTO_PATH,
            url_relative_path='photos/',
            thumbnail_size=(256, 256, True))
    }
    can_export = True
