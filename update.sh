#!/usr/bin/env bash

rm -rf  /var/www/qabattle/*
cp templates/* /var/www/qabattle/

rm -rf /etc/nginx/sites-enabled/
chmod 644 qabattle
cp qabattle /etc/nginx/sites-enabled/qabattle

systemctl restart nginx
