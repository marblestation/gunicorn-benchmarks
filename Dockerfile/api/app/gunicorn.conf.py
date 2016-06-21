import multiprocessing, os

#bind = 'unix:/tmp/gunicorn.benchmark.sock'
bind = '0.0.0.0:80'
workers = 1
max_requests = 200
timeout = 30
preload_app = True
chdir = os.path.dirname(__file__)
daemon = False
debug = False
loglevel = 'DEBUG'
backlog = 2048

errorlog = '{}/benchmark.error.log'.format(os.getcwd())
accesslog = '{}/benchmark.access.log'.format(os.getcwd())
pidfile = '/tmp/gunicorn-benchmark.pid'

worker_class = 'sync'
