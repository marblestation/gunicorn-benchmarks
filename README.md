# Benchmark

# Setup
Install:
  * VirtualBox
  * vagrant

Then simply:

```bash
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
python3 hammer.py -c 21 -n 50 --sleep 0 --endpoint service2
```

# Test 2

Hammer the server with the following route:

client -> VM1 -> VM2 -> VM1 -> client

```bash
python3 hammer.py -c 21 -n 50 --sleep 0 --endpoint service
```

