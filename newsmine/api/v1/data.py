"""
Data route.

It provides data APIs.
"""


import requests
import logging

from flask import Blueprint, jsonify

from config import CONFIG

LOGGER = logging.getLogger(__name__)
API = Blueprint('data', __name__, url_prefix='/v1/data')

NEWS_API = CONFIG['API']['url.naverdev.news']
CLIENT_ID = CONFIG['VAL']['naverdev.client.id']
CLIENT_SECRET = CONFIG['VAL']['naverdev.client.secret']


@API.route('/mynews/<query>')
def mynews(query):
    display, sort = 10, 'sim'
    try:
        resp = requests.get(
            url=NEWS_API,
            params={
                'query': query,
                'display': display,
                'sort': sort,
            },
            headers={
                'X-Naver-Client-Id': CLIENT_ID,
                'X-Naver-Client-Secret': CLIENT_SECRET,
            },
        )
    except requests.RequestException as re:
        raise re

    result = {'status_code': resp.status_code}
    if resp.status_code == 200:
        for key in resp.json():
            result[key] = resp.json()[key]
        result['result'] = 'Success'
    else:
        result['result'] = 'Fail'
    return jsonify(data=result)
