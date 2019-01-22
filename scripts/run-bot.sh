#!/usr/bin/env bash

echo ${CONTAINER_TIMEZONE} >/etc/timezone && \
dpkg-reconfigure -f noninteractive tzdata
echo "Container timezone set to: $CONTAINER_TIMEZONE"


echo "start bot"
source environment_vars.sh

python bot_main.py
