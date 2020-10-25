import requests
import logging

from flask import Blueprint, jsonify

LOGGER = logging.getLogger(__name__)
API = Blueprint('data', __name__, url_prefix='/v1/data')

NAVER_DEV_API = 'https://openapi.naver.com/v1/search/news'
CLIENT_ID = ''
CLIENT_SECRET = ''


@API.route('/mynews/<query>')
def mynews(query):
    display, sort = 10, 'sim'
    try:
        resp = requests.get(
            url=NAVER_DEV_API,
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
