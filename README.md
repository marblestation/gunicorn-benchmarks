# Benchmark

# Setup
Install:
  * [Anaconda](https://www.continuum.io/downloads)
  * [VirtualBox](https://www.virtualbox.org/)
  * [Vagrant](https://www.vagrantup.com/)

Then simply:

```bash
$ virtualenv python
$ source python/bin/activate
$ pip install -r requirements.txt
```

# Start VM1 (api)

```bash
vagrant up api
```

# Start VM2 (service)

```bash
vagrant up service
```

# Test 1

Hammer the server with the following route:

client -> VM1 -> VM2 -> client

```bash
python hammer.py -c 21 -n 50 --sleep 0 --endpoint service2
```

# Test 2

Hammer the server with the following route:

client -> VM1 -> VM2 -> VM1 -> client

```bash
python hammer.py -c 21 -n 50 --sleep 0 --endpoint service
```

# Finer control

Go into the corresponding dockers:

```bash
vagrant ssh api
docker exec -it api /bin/bash
```

```bash
vagrant ssh service
docker exec -it service /bin/bash
```

Stop the service in both dockers:

```bash
mv /etc/service/gunicorn/ /etc/disabled_gunicorn/
pkill -f "runsv gunicorn"
```

Manually start the service in both dockers:

```bash
pkill -f gunicorn
export GUNICORN_WORKERS=1
export GUNICORN_THREADS=1
export GUNICORN_WORKER_CLASS="sync"
cd /app
gunicorn -c gunicorn.conf.py wsgi:application
```
