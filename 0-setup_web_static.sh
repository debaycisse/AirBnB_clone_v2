#!/usr/bin/env bash
# script sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
if ! dpkg -s nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html &> /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
NGINX_CONFIG="/etc/nginx/sites-available/default"
sudo sed -i "/^\s*location \/hbnb_static\s*{/a \ \ \ \ alias /data/web_static/current/;" "$NGINX_CONFIG"

# Restart Nginx
sudo service nginx restart

