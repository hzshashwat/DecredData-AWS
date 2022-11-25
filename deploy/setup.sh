#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/hzshashwat/DecredData-AWS.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/decreddata

mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/decreddata

$VIRTUALENV_BASE_PATH/decreddata/bin/pip install -r $PROJECT_BASE_PATH/profiles-rest-api/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/decreddata/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/decreddata/deploy/supervisor_decreddata.conf /etc/supervisor/conf.d/decreddata.conf
supervisorctl reread
supervisorctl update
supervisorctl restart decreddata

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/decreddata/deploy/nginx_decreddata.conf /etc/nginx/sites-available/decreddata.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/decreddata.conf /etc/nginx/sites-enabled/decreddata.conf
systemctl restart nginx.service

echo "DONE! :)"
