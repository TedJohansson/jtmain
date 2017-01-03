 FROM python:3.6-slim
 RUN apt-get update -y
 RUN apt-get install -y gcc libpq-dev postgresql-client postgresql-client-common
 RUN mkdir /config
 ADD /config/requirements.py /config/
 RUN pip install -r /config/requirements.py
 RUN mkdir /src;
 WORKDIR /src
