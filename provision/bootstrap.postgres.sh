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
pushd /vagrant/Dockerfile/postgres
docker rmi postgres
docker build --tag postgres .
popd
docker rm -f postgres
docker run -d --hostname postgres --name postgres -p 5432:5432  postgres

echo "Waiting 15s for postgres to start..."
sleep 15


for x in api service
do
  echo "Adding database $x"

  docker exec -i postgres psql -U postgres -c "CREATE DATABASE $x;"
  docker exec -i postgres psql -U postgres -c "CREATE USER $x PASSWORD '$x';"
  docker exec -i postgres psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $x TO $x;"

done
