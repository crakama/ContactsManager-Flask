import os
#from app import contactsapp
from app import create_app, db
#from app.models import User, Role
from app.models import User
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
contactsapp = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(contactsapp)
migrate = Migrate(contactsapp, db)


def make_shell_context():
	return dict(app=contactsapp, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
	"""Run the unit tests."""

import unittest
tests = unittest.TestLoader().discover('tests')
unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
	manager.run()
