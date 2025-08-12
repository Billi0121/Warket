FROM python:3.13-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY warket/ /app

WORKDIR /app

CMD [ "python", "manage.py", "runserver"]