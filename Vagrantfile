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

  # VM 1
  config.vm.define :api do |api|
    # Define box
    api.vm.box = "ubuntu/trusty64"
    api.vm.network :private_network, ip: "10.0.0.10"
    api.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
    api.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
     vb.cpus = 1
    end
    # Provision
    api.vm.provision :shell, :path => "./provision/bootstrap.api.sh"
  end

  # VM 2
  config.vm.define :service do |service|
    # Define box
    service.vm.box = "ubuntu/trusty64"
    service.vm.network :private_network, ip: "10.0.0.11"
    service.vm.network "forwarded_port", guest: 80, host: 8081, auto_correct: true
    service.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
     vb.cpus = 1
    end
    # Provision
    service.vm.provision :shell, :path => "./provision/bootstrap.service.sh"
  end

end
