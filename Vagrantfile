$script = <<-SCRIPT
sudo yum install -y https://repo.ius.io/ius-release-el7.rpm
echo "Run update"
sudo yum update
echo "Install python 3.6"
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
sudo yum install python2-pycodestyle
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.synced_folder '.', '/home/vagrant/adyen-python-api-library', disabled: false
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.network :forwarded_port, guest:3001, host: 3001
  config.vm.provider :virtualbox do |vb|
       vb.name = "adyen-python-api-library"
       vb.customize ["modifyvm", :id, "--memory", "1024", "--cpus", "2"]
   end
  config.vm.provision "shell", inline: $script
end