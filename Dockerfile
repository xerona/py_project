FROM python:3.7-slim

RUN apt-get update
RUN apt-get install -y git-core curl build-essential openssl libssl-dev
RUN curl -fsSL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs

RUN mkdir /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app/server
RUN pip install -r requirements.txt

WORKDIR /usr/src/app
RUN npm install

CMD python /usr/src/app/server/app.py & npm run watch --prefix /usr/src/app
