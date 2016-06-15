#!/usr/bin/env python
# encoding: utf-8
import time
import random
import requests
import argparse

from multiprocessing import Pool


def http_get(url):
    """
    Make request to a given
    :param url: URL
    """
    t_received = time.gmtime().tm_sec
    t_start = time.time()
    r = requests.get(url, timeout=360)
    t_end = time.time()

    return {
        'code': r.status_code,
        'time': '{} ms'.format(t_end - t_start),
        'sleep': r.text,
        'start_time': t_received
    }


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port', dest='port', default=8080
    )
    parser.add_argument(
        '--endpoint', dest='endpoint', default='service'
    )
    parser.add_argument(
        '--sleep', dest='sleep', default=0, type=int
    )
    parser.add_argument(
        '-c', '--concurrency', dest='concurrency', default=1, type=int
    )
    parser.add_argument(
        '-n', '--requests', dest='requests', default=10, type=int
    )

    args = parser.parse_args()

    print('Number of users: {}'.format(args.concurrency))
    print('Number of requests: {}'.format(args.requests))
    print('Maximum forced sleep: {}'.format(args.sleep))

    api_url = []
    for i in range(args.requests * args.concurrency):

        sleep = int(random.random() * args.sleep)

        api_url.append(
            'http://localhost:{port}/{endpoint}/{sleep}'
            .format(
                port=args.port,
                endpoint=args.endpoint,
                sleep=sleep
            )
        )

    pool = Pool(processes=args.concurrency)

    results = pool.map(http_get, api_url)

    print('Number of requests: {}'.format(len(results)))
    print('Number of 200s: {}'
          .format(len([i for i in results if i['code'] == 200])))
    print('Number of 500s: {}'
          .format(len([i for i in results if i['code'] >= 500])))

    # should_print = any([i['code'] > 200 for i in results])
    # if should_print:
    #     for result in results:
    #         print(result)

