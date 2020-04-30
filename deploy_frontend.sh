#!/bin/bash

cd /home/ubuntu/csci-4145-project-frontend &&
npm run build &&
sudo cp -R dist/* /var/www/html
