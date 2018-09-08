import os
from flask import (
    Flask, current_app, send_file,
    send_from_directory
)

from .api import api_bp
from .client import client_bp

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin.contrib.sqla import ModelView
import flask_admin as admin

app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)
# app.register_blueprint(client_bp)

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from .models import *

admin = admin.Admin(app, name='Eat•In•Der', template_mode='bootstrap3')

admin.add_view(ModelView(Label, db.session, name="Labels"))
admin.add_view(MealView(Meal, db.session, name="Meals"))
admin.add_view(UserView(User, db.session, name="Users"))

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)

# Static paths
@app.route('/static/photos/<path:path>')
def static_photos(path):
    return send_from_directory(Config.PHOTO_PATH, path)
