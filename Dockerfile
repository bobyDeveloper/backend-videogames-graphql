FROM python:3
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1

RUN mkdir /videogames
WORKDIR /videogames
COPY requirements.txt /videogames/
RUN pip install -r requirements.txt

COPY . /videogames/
CMD python manage.py runserver 0.0.0.0:8080