#!/usr/bin/env python

import time
import requests
from multiprocessing import Process, Pool

concurrency = 500

url = ['http://localhost:5001/benchmark'] * concurrency

def millis():
  return int(round(time.time() * 1000))

def http_get(url):
  start_time = millis()
  r = requests.get(url)
  result = {"code": r.status_code, "time": "{} ms".format(millis() - start_time), "sleep": r.text}
  return result
  
pool = Pool(processes=concurrency)

start_time = millis()
results = pool.map(http_get, url)

print('Number of requests: {}'.format(len(results)))
print('Number of 200s: {}'.format(len([i for i in results if i['code'] == 200])))
print('Number of 500s: {}'.format(len([i for i in results if i['code'] >= 500])))

for result in results:
    if result['code'] >= 500:
        print(result['sleep'])

