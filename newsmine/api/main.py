import logging

from flask import Blueprint, jsonify, \
    make_response, redirect

LOGGER = logging.getLogger(__name__)
API = Blueprint('main', __name__)


@API.route('/test')
def test():
    LOGGER.info('Call test.')
    return jsonify(data='[TEST] Hello, Newsmine!')


# --- Page APIs --- #


@API.route('/main')
def main():
    LOGGER.info('Call main.')
    return jsonify(data='This is main page!')


# --- Redirect APIs --- #


@API.route('/')
def root():
    LOGGER.info('Call root. redirect to main.')
    resp = make_response(redirect('/main'))
    return resp


@API.route('/admin')
def admin():
    LOGGER.info('Call admin. redirect to admin version v1.')
    resp = make_response(redirect('/api/v1/admin'))
    return resp


@API.route('/data')
def data():
    LOGGER.info('Call data. redirect to data version v1.')
    resp = make_response(redirect('/api/v1/data'))
    return resp
