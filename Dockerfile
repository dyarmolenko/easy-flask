FROM python:3.9
COPY /requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /
COPY /app /app

ENV FLASK_APP=app

ENV FLASK_ENV=development

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_RUN_PORT=80

CMD ["flask", "run"]