web: gunicorn example_project.wsgi --log-file -
worker_and_beat: celery -A swiftwind_heroku worker --beat -l info
worker: celery -A swiftwind_heroku worker --beat -l info
beat: celery -A swiftwind_heroku beat -l info
