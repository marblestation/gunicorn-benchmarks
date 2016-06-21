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


class BenchmarkView(Resource):
    """
    Benchmark of Gunicorn end point
    """

    def post(self):
        """
        GET response
        """
        r_data = get_post_data(request)
        sleep = r_data.get('sleep', 0)
        start_time = time.gmtime().tm_sec
        time.sleep(sleep)

        r_data['last_sent'] = 'api/benchmark'
        r_data['sent_from'].append('api/benchmark')
        r_data['service'] = {
            'received_time': start_time,
            'sleep': sleep
        }

        return r_data, 200


class ServiceView(Resource):
    """
    External service view:
    Contacts a second service that will contact the API at the /benchmark
    end point.
    """
    def post(self):

        post_data = get_post_data(request)
        post_data['last_sent'] = 'api/service'
        post_data['sent_from'].append('api/service')

        if 'sleep' not in post_data:
            post_data['sleep'] = 0

        # Post to the end point
        r = requests.post(
            'http://{ip}/benchmark'.format(
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


class ServiceView2(Resource):
    """
    External service view:
    Contacts a second service that will send a simple response (no further
    communication, unlike ServiceView).
    """
    def post(self):

        post_data = get_post_data(request)
        post_data['last_sent'] = 'api/service2'
        post_data['sent_from'].append('api/service2')

        if 'sleep' not in post_data:
            post_data['sleep'] = 0

        # Post to the end point
        r = requests.post(
            'http://{ip}/benchmark2'.format(
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
