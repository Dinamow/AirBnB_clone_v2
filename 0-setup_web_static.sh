#!/usr/bin/env bash
# install nginx

sudo apt-get update
if ! [ -x "$(command -v nginx)" ]; then
	sudo apt-get install nginx -y
fi

sudo mkdir -p data/web_static/releases/test/
sudo mkdir -p data/web_static/shared/
sudo touch data/web_static/releases/test/index.html
echo "<html>
	<head>
	</head>
	<body>
		<p>Hello World!</p>
	</body>
</html>" | sudo tee  data/web_static/releases/test/index.html

sudo rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_file="/etc/nginx/sites-available/default"
sed -i '/hbnb_static/d' "$config_file"

echo "
location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
}" >> "$config_file"

sudo service nginx restart
