FROM python:3.7-alpine

RUN apk add --no-cache bash

# set timezone
RUN apk add --update tzdata
ENV TZ=Europe/Helsinki
RUN rm -rf /var/cache/apk/*

RUN mkdir -p /usr/app
ADD . /usr/app/
WORKDIR /usr/app

ENV CONTAINER_TIMEZONE Europe/Helsinki
RUN pip install -r requirements.txt

CMD ./scripts/run-bot.sh
