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
from models import Foo, db

#from flask.ext.ratelimiter import ratelimit
from limiter import ratelimiter

# Set rate limits
N_REQUESTS = 10000
PER_SECOND = 100
# over_limit=lambda x: "Rate limit was exceeded", 429
# scope_func=lambda: request.remote_addr,
# key_func=lambda: request.endpoint

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

def store_in_db(post_data):
    #db.session.begin() # This fails saying that a transaction has already been opened
    foo = Foo(
                last_sent=str(post_data['last_sent']), \
                client=str(post_data['client']), \
                sent_from=str(post_data['sent_from']), \
                service=str(post_data.get('service', "-")), \
                sleep=int(post_data['sleep'])
            )
    db.session.add(foo)
    db.session.commit() # If this is commented and SQLALCHEMY_COMMIT_ON_TEARDOWN=False, commit does not happen and changes are not saved to PostgreSQL

class ApiEndView(Resource):
    """
    View that returns a response.
    """
    decorators = [ratelimiter.limit("1000/second", methods=['post'])] # Flask Limiter

    #@ratelimit(N_REQUESTS, PER_SECOND) # Flask RateLimiter (DEPRECATED)
    def post(self):
        """
        GET response
        """
        post_data = get_post_data(request)
        sleep = post_data.get('sleep', 0)
        start_time = time.gmtime().tm_sec
        time.sleep(sleep)

        post_data['last_sent'] = 'api/end'
        post_data['sent_from'].append('api/end')
        post_data['service'] = {
            'received_time': start_time,
            'sleep': sleep
        }
        store_in_db(post_data) # INSERT in PostgreSQL without forced sleep

        ## gunicorn automatically monkey-patches when async worker is used: gevent.sleep(x)
        #time.sleep(10)

        #from sqlalchemy import text
        #sql = text("SELECT sent_from FROM foo, pg_sleep(10);")
        #result = db.session.execute(sql)
        ##sent_from = []
        ##for row in result:
            ##sent_from.append(row[0])


        return post_data, 200


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

        store_in_db(post_data) # INSERT in PostgreSQL without forced sleep

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
