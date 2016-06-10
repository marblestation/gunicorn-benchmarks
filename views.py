# encoding: utf-8
"""
Views
"""
import time
import random
from flask.ext.restful import Resource


class BenchmarkView(Resource):
    """
    Benchmark of Gunicorn end point
    """

    def get(self):
        """
        GET response
        """
        sleep_time = random.random() * 3
        #time.sleep(sleep_time)

        return {'sleep': '{}'.format(sleep_time)}, 200


