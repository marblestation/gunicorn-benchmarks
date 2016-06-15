import multiprocessing, os

#bind = 'unix:/tmp/gunicorn.benchmark.sock'
bind = '0.0.0.0:80'
workers = 8
max_requests = 200
timeout = 30
preload_app = True
chdir = os.path.dirname(__file__)
daemon = False
debug = False
loglevel = 'DEBUG'
backlog = 2048

errorlog = '/tmp/benchmark.error.log'
accesslog = '/tmp/benchmark.access.log'
pidfile = '/tmp/gunicorn-benchmark.pid'

worker_class = 'sync'
