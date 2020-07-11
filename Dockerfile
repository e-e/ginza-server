FROM python:3.8.3-buster

WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install ginza
RUN /opt/venv/bin/pip install Flask

COPY src .

ENV FLASK_APP=server.py

ENTRYPOINT /bin/bash -c "source /opt/venv/bin/activate; flask run --host 0.0.0.0"
