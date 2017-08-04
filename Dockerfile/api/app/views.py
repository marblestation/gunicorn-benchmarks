# encoding: utf-8
"""
Views
"""
import time
import json
import requests

from flask import request
from flask.ext.restful import Resource
from config import SERVICE_IP


def get_post_data(request):
    """
    Attempt to coerce POST json data from the request, falling
    back to the raw data if json could not be coerced.
    :param request: flask.request
    """
    try:
        post_data = request.get_json(force=True)
    except:
        post_data = request.values

    post_data = dict(post_data)
    return post_data


class ApiEndView(Resource):
    """
    View that returns a response.
    """

    def post(self):
        """
        GET response
        """
        r_data = get_post_data(request)
        sleep = r_data.get('sleep', 0)
        start_time = time.gmtime().tm_sec
        time.sleep(sleep)

        r_data['last_sent'] = 'api/end'
        r_data['sent_from'].append('api/end')
        r_data['service'] = {
            'received_time': start_time,
            'sleep': sleep
        }

        return r_data, 200


class ApiRedirectView(Resource):
    """
    View that contacts a second service which will return a response.
    """
    def post(self):

        post_data = get_post_data(request)
        post_data['last_sent'] = 'api/double_redirect'
        post_data['sent_from'].append('api/double_redirect')

        if 'sleep' not in post_data:
            post_data['sleep'] = 0

        # Post to the end point
        r = requests.post(
            'http://{ip}/service_end'.format(
                ip=SERVICE_IP
            ),
            data=json.dumps(post_data)
        )

        # Get the response content if there was no failure
        try:
            _json = r.json()
        except:
            _json = {'msg': r.text}

        return _json, r.status_code


class ApiDoubleRedirectView(Resource):
    """
    View that contacts a second service that will contact the API and
    return a response.
    """
    def post(self):

        post_data = get_post_data(request)
        post_data['last_sent'] = 'api/redirect'
        post_data['sent_from'].append('api/redirect')

        if 'sleep' not in post_data:
            post_data['sleep'] = 0

        # Post to the next point
        r = requests.post(
            'http://{ip}/service_redirect'.format(
                ip=SERVICE_IP
            ),
            data=json.dumps(post_data)
        )

        # Get the response content if there was no failure
        try:
            _json = r.json()
        except:
            _json = {'msg': r.text}

        return _json, r.status_code
