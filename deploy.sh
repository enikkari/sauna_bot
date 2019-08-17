#!/usr/bin/env bash
export version="add-webapp-8000-info"

docker build -t futurice/saunabot:$version .

export SSH_KEY=~/.ssh/id_rsa_futuswarm

playswarm image:push -i futurice/saunabot -t $version

playswarm app:deploy -i futurice/saunabot -t $version -n saunabot