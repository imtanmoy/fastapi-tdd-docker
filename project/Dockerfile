# pull official base image
FROM python:3.8.5-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile

# add app
COPY . .