#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment of web_static
if ! command -v nginx &>/dev/null; then
        sudo apt-get update
        sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test

sudo mkdir -p /data/web_static/shared

printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration
NGINX_CONFIG="/etc/nginx/sites-available/default"

sed -i 's/server_name _;/server_name debaycisse.tech;/g' "$NGINX_CONFIG"

sed -i '48,52d' "$NGINX_CONFIG"

sed -i '48i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' "$NGINX_CONFIG"

# Restart Nginx
sudo service nginx restart
