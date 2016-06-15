# encoding: utf-8
"""
Views
"""
import time
import random
import requests

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
    External service view
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
    External service view
    """
    def get(self, sleep):

        r = requests.get('{}/{}'.format(SERVICE_IP_2, sleep))
        try:
            _json = r.json()
        except:
            _json = {'msg': r.text}

        return _json, r.status_code
