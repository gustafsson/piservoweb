#!/bin/bash

set -e

if [ ! -f mypi ]; then
	echo 'Create a file named "mypi" with the user name and ip adress of your pi. Like pi@192.168.0.21'
	false
fi

mypi=$(cat mypi)
scp piservo3.py ${mypi}:~/dev/piservo
ssh ${mypi} 'cd ~/dev/piservo;sudo python piservo3.py'
