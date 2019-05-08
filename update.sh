#!/usr/bin/env bash

rm -rf  /var/www/qabattle/*
cp templates/* /var/www/qabattle/

systemctl restart nginx
