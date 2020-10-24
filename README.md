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
/project/root/path $ . ./venv/bin/activate
(venv) /project/root/path $ pip install -r requirements.txt
```

## When you start this app

#### Run as development mode

```shell
(venv) /project/root/path $ FLASK_DEBUG=1 FLASK_APP=newsmine/__init__.py flask run
```

#### Run as production

```shell
/project/root/path $ sh run_app.sh
```

## Activate pytest

```shell
(venv) /project/root/path $ ptw  // pytest-watch
```

## Version info

| Tool | Description | Version |
|:--|:--|:--|
| Python | Main lang | 3.6 |
