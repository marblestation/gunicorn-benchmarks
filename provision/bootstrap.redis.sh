#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates

# Docker daemon
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install -y docker-engine
sudo usermod -aG docker vagrant

# docker
pushd /vagrant/Dockerfile/redis
docker rmi redis
docker build --tag redis .
popd
docker rm -f redis
docker run -d --hostname redis --name redis -p 6379:6379  redis


