sudo apt-get install git htop curl -y

#curl -sSL https://get.docker.com | sh
#sudo systemctl enable docker
#sudo systemctl start docker
#sudo usermod -aG docker pi

sudo apt-get update -y && sudo apt-get install -y python3-pip python3-dev
sudo apt-get remove docker docker-engine docker.io
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh
#sudo pip3 install docker-compose
sudo pip3 install -U docker-compose
#sudo docker-compose -f docker-compose-profess.yml pull ofw
sudo usermod -a -G docker $USER
sudo reboot

