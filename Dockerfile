FROM python:3.8-slim-buster
COPY . /code
RUN pip install -r /code/requirements.txt
WORKDIR /code
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000