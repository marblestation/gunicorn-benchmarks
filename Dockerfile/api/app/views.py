# encoding: utf-8
"""
Views
"""
import time
import json
import requests

from flask import request
from flask.ext.restful import Resource
from config import SERVICE_IP, SERVICE_IP_2


class BenchmarkView(Resource):
    """
    Benchmark of Gunicorn end point
    """

    def get(self, sleep):
        """
        GET response
        """
        start_time = time.gmtime().tm_sec
        time.sleep(sleep)

        return {'sleep': '{}'.format(sleep), 'received_time': start_time, 'name': 'api'},


class ServiceView(Resource):
    """
    External service view:
    Contacts a second service that will contact the API at the /benchmark
    end point.
    """
    def get(self, sleep):

        r = requests.get('{}/{}'.format(SERVICE_IP, sleep))
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

        post_data = request.get_json(force=True)
        post_data['last_sent'] = 'api'
        post_data['sent_from'].append('api')

        if 'sleep' not in post_data:
            post_data['sleep'] = 0

        # Post to the end point
        r = requests.post(
            'http://{ip}/benchmark2'.format(
                ip=SERVICE_IP_2
            ),
            data=json.dumps(post_data)
        )

        # Get the response content if there was no failure
        try:
            _json = r.json()
        except:
            _json = {'msg': r.text}

        return _json, r.status_code
