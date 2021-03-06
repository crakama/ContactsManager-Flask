
from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO
from app import create_app
from app import db
import os.path

app = create_app('development')
with app.app_context():
	#Instructs SQLAlchemy to create DB based on model classes
	db.create_all()

	#
	if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
	    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
	    api.version_control(app.config['SQLALCHEMY_DATABASE_URI'], SQLALCHEMY_MIGRATE_REPO)
	else:
	    api.version_control(app.config['SQLALCHEMY_DATABASE_URI'], SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))