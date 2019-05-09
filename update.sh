#!/usr/bin/env bash

pip install -r requirements.txt -y

rm -rf  /var/www/qabattle/*
cp -r templates/* /var/www/qabattle/

rm -rf /etc/nginx/sites-enabled/*
chmod 644 qabattle
cp qabattle /etc/nginx/sites-enabled/qabattle

systemctl restart nginx

rm -rf /etc/init/qabattle.conf
cp qabattle.conf  /etc/init/qabattle.conf
