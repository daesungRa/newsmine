import logging

from flask import Blueprint, jsonify, request

LOGGER = logging.getLogger(__name__)
API = Blueprint('data', __name__, url_prefix='/api/v1/data')


@API.route('/')
def data():
    LOGGER.info('Call data!')
    return jsonify(data='Call data.')
