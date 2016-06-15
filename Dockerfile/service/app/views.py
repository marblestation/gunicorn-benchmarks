# encoding: utf-8
"""
Views
"""
import time
import random
import requests

from flask.ext.restful import Resource
from config import SERVICE_IP


class BenchmarkView(Resource):
    """
    Benchmark of Gunicorn end point
    """

    def get(self, sleep):
        """
        GET response
        """

        r = requests.get('{}/{}'.format(SERVICE_IP, sleep))
        try:
            _json = r.json()
        except:
            _json = {'msg': r.text}

        start_time = time.gmtime().tm_sec
        time.sleep(sleep)

        return {'sleep': '{}'.format(sleep), 'received_time': start_time, 'name': 'service', 'from_api': _json}, 200


class BenchmarkView2(Resource):
    """
    Benchmark of Gunicorn end point
    """

    def get(self, sleep):
        """
        GET response
        """

        start_time = time.gmtime().tm_sec
        time.sleep(sleep)

        return {'sleep': '{}'.format(sleep), 'received_time': start_time, 'name': 'service'}, 200
