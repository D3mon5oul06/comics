FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /Hackernews
WORKDIR /comics
COPY requirements.txt /Hackernews/
RUN pip install -r requirements.txt
COPY . /Hackernews/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080
