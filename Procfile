release: ./manage.py migrate --no-input
web: gunicorn swiftwind_heroku.wsgi --log-file -
worker_and_beat: celery -A swiftwind_heroku worker --beat -l info
worker: celery -A swiftwind_heroku worker --beat -l info
beat: celery -A swiftwind_heroku beat -l info
