# Newsmine

Newsmine is based on the [Flask](https://github.com/pallets/flask) project owned by [pallets team](https://github.com/pallets). This project aims to provide a collection of news of your choice.

**Anyone can modify and distribute this project.**

## Structure

## Installation

> At least python ```version 3.6``` or higher is recommended.

> Clone this github project to your desktop root path.

```shell
/project/root/path $ pip install -U virtualenv
/project/root/path $ virtualenv venv
/project/root/path $ . ./venv/bin/activate  # . ./venv/Scripts/activete (on windows)
(venv) /project/root/path $ pip install -r requirements.txt
```

## When you start this app

#### Run as development mode

```shell
# on ubuntu
(venv) /project/root/path $ FLASK_DEBUG=1 FLASK_APP=newsmine/__init__.py flask run

# on windows
(venv) /project/root/path $ set FLASK_ENV=development
(venv) /project/root/path $ set FLASK_APP=newsmine/__init__.py
(venv) /project/root/path $ flask run
```

#### Run as production

```shell
# on ubuntu
/project/root/path $ sh run_app.sh

# on windows
## run as development mode is recommanded.
```

## Activate pytest

```shell
(venv) /project/root/path $ ptw  // pytest-watch
```

## Version info

| Tool | Description | Version |
|:--|:--|:--|
| Python | Main lang | 3.6 |
| Ubuntu | OS | 18.04 |
