import logging

from flask import Blueprint, jsonify, make_response, redirect

from newsmine.db.mysql.users import Users
from newsmine.db.redis.session import Session

LOGGER = logging.getLogger(__name__)
API = Blueprint('main', __name__, url_prefix='/')


@API.route('/test')
def test():
    LOGGER.info('Call test.')
    return jsonify(data='[TEST] Hello, Newsmine!')


@API.route('')
def root():
    LOGGER.info('Call root. redirect to main.')
    resp = make_response(redirect('/main'))
    return resp


@API.route('/main')
def main():
    LOGGER.info('Call main.')
    return jsonify(data='This is main page!')

