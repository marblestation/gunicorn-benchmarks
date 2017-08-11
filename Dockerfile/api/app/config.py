# 10.0.0.10 is the api
# 10.0.0.11 is the service
SERVICE_IP = '10.0.0.11'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s\t%(process)d '
                      '[%(asctime)s]:\t%(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'formatter': 'default',
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#### http://flask-sqlalchemy.pocoo.org/2.1/config/
# A dictionary that maps bind keys to SQLAlchemy connection URIs.
SQLALCHEMY_BINDS = None
# Version 2.0 (August 29th 2014) changelog: Consider SQLALCHEMY_COMMIT_ON_TEARDOWN harmful and remove from docs.
# http://flask-sqlalchemy.pocoo.org/2.1/changelog/
# https://stackoverflow.com/questions/23301968/invalid-transaction-persisting-across-requests
#SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# The database URI that should be used for the connection.
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://api:api@10.0.0.12:5432/api"
# If set to True SQLAlchemy will log all the statements issued to stderr which can be useful for debugging.
SQLALCHEMY_ECHO = False
# The size of the database pool. Defaults to the engine's default (usually 5)
SQLALCHEMY_POOL_SIZE = 5
# Number of seconds after which a connection is automatically recycled. This is required for MySQL, which removes connections after 8 hours idle by default. Note that Flask-SQLAlchemy automatically sets this to 2 hours if MySQL is used.
SQLALCHEMY_POOL_RECYCLE = 300
# Controls the number of connections that can be created after the pool reached its maximum size. When those additional connections are returned to the pool, they are disconnected and discarded.
SQLALCHEMY_MAX_OVERFLOW = 10
# If set to True, Flask-SQLAlchemy will track modifications of objects and emit signals. The default is None, which enables tracking but issues a warning that it will be disabled by default in the future. This requires extra memory and should be disabled if not needed.
SQLALCHEMY_TRACK_MODIFICATIONS = False

## https://pythonhosted.org/Flask-Caching/
#CACHE = {
#            u'CACHE_REDIS_PORT': 6379,
#            u'CACHE_TYPE': u'redis',
#            u'CACHE_REDIS_HOST': u'10.0.0.13',
#            u'CACHE_REDIS_DB': 0,
#            u'CACHE_KEY_PREFIX': u'api_'
#        }
RATELIMITER_BACKEND = "flaskcacheredis"
RATELIMITER_BACKEND_OPTIONS = {u'host': u'10.0.0.13', u'db': 0, u'port': 6379}
RATELIMITER_INJECT_X_HEADERS = True
RATELIMITER_KEY_PREFIX = "rate_limit"

RATELIMIT_STORAGE_URL = "redis://10.0.0.13:6379"
RATELIMIT_HEADERS_ENABLED = True
RATELIMIT_KEY_PREFIX = "limiter"
