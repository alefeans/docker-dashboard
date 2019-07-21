FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b :8000", "-w 3", "--access-logfile", "-", "--error-logfile", "-", "docker_dashboard.wsgi:application"]