#!/usr/bin/env bash
# Setup static
sudo apt-get update
sudo apt-get install nginx
[[ ! -d /data ]] && sudo mkdir /data
[[ ! -d /data/web_static ]] && sudo mkdir /data/web_static
[[ ! -d /data/web_static/releases ]] && sudo mkdir /data/web_static/releases
[[ ! -d /data/web_static/shared ]] && sudo mkdir /data/web_static/shared
[[ ! -d /data/web_static/releases/test ]] && sudo mkdir /data/web_static/releases/test
[[ ! -f /data/web_static/releases/test/index.html ]] && sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
    </head>
    <body>
      Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '51i\\tlocation \/hbnb_static {alias /data/web_static/current;}' /etc/nginx/sites-available/default
sudo service nginx restart
exit $?
