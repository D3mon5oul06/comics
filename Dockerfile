FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /Hackernews
WORKDIR /comics
COPY requirements.txt /comics/
RUN pip install -r requirements.txt
COPY . /comics/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080
