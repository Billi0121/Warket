FROM python:3.13-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY warket/ /app

WORKDIR /app

# CMD [ "python", "manage.py", "runserver" ]
CMD [ "gunicorn", "warket.wsgi:application", "--bind", "0:8000"]