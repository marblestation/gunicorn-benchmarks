# Benchmark

```
# Start nginx
docker run --name nginx-bench -v `pwd`/nginx.conf:/etc/nginx/nginx.conf:ro -d -p 5000:80 -v /tmp/:/tmp/:ro nginx
# Start gunicorn
gunicorn -c gunicorn.conf.py wsgi:application

# Run test
python hammer.py
```
