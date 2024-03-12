pytohn manage.py collectstatic --no-input

guvicorn core.wsgi:application --bind 0.0.0.0:8000