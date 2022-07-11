FROM python:3.10
RUN PYTHONUNBUFFERED=1
RUN mkdir /code
RUN apt-get update \
    && apt-get install -y postgresql-client
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY . /code/
WORKDIR /code/link_shot_project
