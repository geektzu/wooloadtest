#! /bin/bash

# for installaion at Ubuntu

sudo apt -y update
sudo apt-get install python3
sudo apt install python3-pip
pip3 install selenium
pip3 install Faker
#sudo apt install google-chrome-stable

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

