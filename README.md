<!-- need to install:
virtualenv
pip
python3 inside virtualenv project
uwsgi
flask -->
## Setup Machine Environement

1.  Different projects often require different versions of Node.
    It is important to install Node via a version manager so that different versions can co-exist on your system.

    Linux and MacOS users should install [nvm](https://github.com/creationix/nvm).

            $ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash

    The installer tries to modify your your `~/.bash_profile`, `~/.zshrc`, `~/.profile`, or `~/.bashrc`.
    You will need to open a new shell or terminal for the changes to take effect.

    Verify that nvm was installed.

            $ command -v nvm

    Windows users can install [nvm-windows](https://github.com/coreybutler/nvm-windows).

    Verify that nvm was installed.

            <user@user>: nvm

2. Install Node LTS version - this project developed with lts/dubnium.

            $ nvm install <VERSION>
            $ nvm use <VERSION>

3. Install docker
  $ sudo apt-get update
  $ sudo apt-get install docker-ce
<!-- docker -v
Docker version 18.06.1-ce, build e68fc7a
-->


4. Install Pip3
  1. sudo apt update
  2. sudo apt install python3-pip

  Verify pip3 installed
    1. pip3 --version

4. Install Virtualenv using Pip3
  1. sudo pip3 install virtualenv

  Verify Virtualenv installed
    1. virtualenv --version

##SETUP FLASK Environment
3. virtualenv <name_of_env>
4. source <name_of_env>/bin/activate
5. pip3 install -r requirements.txt

## Start Flask App
FLASK_APP=run.py flask run

##SETUP NODE Modules

1. npm ci



Will need to download Cards Json file from <a href="https://mtgjson.com/">https://mtgjson.com</a>
Make sure the download file is called "AllCards.json"
Place file under root of back_end directory

## Build docker image using docker-compose
docker-compose -f docker-compose.yml -f docker-compose.local.yml build --no-cache
docker-compose -f docker-compose.yml -f docker-compose.local.yml build
docker-compose up

## Running python tests command line
coverage run -m --include */card-collection/back_end/* unittest discover
coverage html
