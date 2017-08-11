# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # VM 0
  config.vm.define :postgres do |postgres|
    # Define box
    postgres.vm.box = "ubuntu/trusty64"
    postgres.vm.hostname = "vagrant-postgres"
    postgres.vm.network :private_network, ip: "10.0.0.12"
    postgres.vm.network "forwarded_port", guest: 5432, host: 15432, auto_correct: true
    postgres.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = 1
    end
    # Provision
    postgres.vm.provision :shell, :path => "./provision/bootstrap.postgres.sh"
  end

  # VM 1
  config.vm.define :redis do |redis|
    # Define box
    redis.vm.box = "ubuntu/trusty64"
    redis.vm.hostname = "vagrant-redis"
    redis.vm.network :private_network, ip: "10.0.0.13"
    redis.vm.network "forwarded_port", guest: 6379, host: 16379, auto_correct: true
    redis.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = 1
    end
    # Provision
    redis.vm.provision :shell, :path => "./provision/bootstrap.redis.sh"
  end

  # VM 2
  config.vm.define :api do |api|
    # Define box
    api.vm.box = "ubuntu/trusty64"
    api.vm.hostname = "vagrant-api"
    api.vm.network :private_network, ip: "10.0.0.10"
    api.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
    api.vm.network "forwarded_port", guest: 5050, host: 5050, auto_correct: true
    api.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = 1
    end
    # Provision
    api.vm.provision :shell, :path => "./provision/bootstrap.api.sh"
  end

  # VM 3
  config.vm.define :service do |service|
    # Define box
    service.vm.box = "ubuntu/trusty64"
    service.vm.hostname = "vagrant-service"
    service.vm.network :private_network, ip: "10.0.0.11"
    service.vm.network "forwarded_port", guest: 80, host: 8081, auto_correct: true
    service.vm.network "forwarded_port", guest: 5050, host: 5051, auto_correct: true
    service.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
        vb.cpus = 1
    end
    # Provision
    service.vm.provision :shell, :path => "./provision/bootstrap.service.sh"
  end
  

end
