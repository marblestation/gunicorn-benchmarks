#!/bin/bash
docker rm -f service
docker run -d --name service -p 5050:80 -v /vagrant:/app/conf:ro -v /tmp:/tmp service

sudo cp nginx.conf /etc/nginx/nginx.conf
sudo service nginx restart

