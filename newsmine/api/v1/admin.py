import logging

from flask import Blueprint, jsonify, request

from newsmine.db.mysql.users import Users
from newsmine.db.redis.session import Session

LOGGER = logging.getLogger(__name__)
API = Blueprint('admin', __name__, url_prefix='/api/v1/admin')


@API.route('')
def admin():
    LOGGER.info('Call admin. check for session..')
    session_cookie = request.cookies.get('session')
    if session_cookie:
        username = Session(session_cookie).username
        if username:
            user_id = Users().get_by_username_or_id(username=username)['id']
            # TODO: Render index.html
            return jsonify(data=f'{username} Already logged in. go to index page.')
    # TODO: Render login.html
    return jsonify(data='No session, please log in first.')


@API.route('/login')
def login():
    LOGGER.info('Call login!')


@API.route('/logout')
def logout():
    LOGGER.info('Call logout!')

