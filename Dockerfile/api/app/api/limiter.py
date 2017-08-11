## Flask RateLimiter (DEPRECATED)
#from flask.ext.ratelimiter import RateLimiter
#ratelimiter = RateLimiter()

## Flask Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
#ratelimiter = Limiter(key_func=get_remote_address, default_limits=["1000 per second"])
ratelimiter = Limiter(key_func=get_remote_address)

