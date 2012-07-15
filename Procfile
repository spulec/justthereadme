web: gunicorn justthereadme.wsgi:application -b 0.0.0.0:$PORT -c justthereadme/gunicorn.conf
celeryd: python manage.py celeryd -E -B --loglevel=INFO