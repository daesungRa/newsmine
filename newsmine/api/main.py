"""
Default main route.

It provides a common page and redirect APIs.
Redirect APIs redirect to v1 path.
"""


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
    resp = make_response(redirect('/v1/admin'))
    return resp


@API.route('/mynews')
def mynews():
    LOGGER.info('Call mynews. redirect to news version v1.')
    sample_query = 'bitcoin'
    resp = make_response(redirect(f'/v1/data/mynews/{sample_query}'))
    return resp
