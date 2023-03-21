Vagrant.configure("2") do |config|
  config.vm.box = "jeffnoxon/ubuntu-20.04-arm64"
  config.vm.synced_folder '.', '/home/vagrant/adyen-python-api-library', disabled: false
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.network :forwarded_port, guest:3001, host: 3001
  config.vm.provider :parallels
end