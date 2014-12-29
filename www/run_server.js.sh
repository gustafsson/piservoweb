#!/bin/bash

set -e

if [ ! -f ../mypi ]; then
	echo 'Create a file named "../mypi" with the user name and ip adress of your pi. Like pi@192.168.0.21'
	false
fi

mypi=$(cat ../mypi)
scp server.js ${mypi}:~/dev/piservo/www
scp -r wwwroot ${mypi}:~/dev/piservo/www/
ssh ${mypi} 'cd ~/dev/piservo/www/wwwroot;sudo npm ../server.js'
