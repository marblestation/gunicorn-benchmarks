#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y install nginx apt-transport-https ca-certificates

# Docker daemon
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install -y docker-engine
sudo usermod -aG docker vagrant

# docker
pushd /vagrant/Dockerfile/service
docker build --tag service .
popd
docker rm -f service
docker run -d --name service -p 5050:80 service

# nginx
sudo cp /vagrant/nginx.conf /etc/nginx/nginx.conf
sudo service nginx start
sudo service nginx restart

