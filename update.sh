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
chmod 644 /qabattle/qabattle.sock
chmod 777 /qabattle

mkdir -p /var/log/qabattle
rm -rf /var/log/qabattle/qabattle.log
touch /var/log/qabattle/qabattle.log

rm -rf /etc/init/qabattle.conf
cp qabattle.conf  /lib/systemd/system/qabattle.service
systemctl enable qabattle
service qabattle restart

service nginx configtest
systemctl restart nginx
