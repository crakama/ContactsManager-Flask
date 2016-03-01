web: gunicorn manage:contactsapp --log-file -
worker: celery -A reminders.celery worker -l info