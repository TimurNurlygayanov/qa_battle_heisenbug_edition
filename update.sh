#!/usr/bin/env bash

pip install -r requirements.txt


rm -rf  /var/www/qabattle/*
cp -r templates/* /var/www/qabattle/


rm -rf /etc/nginx/sites-enabled/*
chmod 644 qabattle
cp qabattle /etc/nginx/sites-enabled/qabattle


rm -rf /qabattle
mkdir /qabattle
touch /qabattle/qabattle.sock

chown www-data:www-data -R /qabattle
chmod 777 -R /qabattle


rm -rf /etc/init/qabattle.conf
cp qabattle.conf  /etc/init/qabattle.conf


service nginx configtest
systemctl restart nginx
