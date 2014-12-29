#!/bin/bash

set -e

if [ ! -f mypi_url ]; then
	echo 'Create a file named "mypi" with the user name and ip adress of your pi. Like pi@192.168.0.21'
	false
fi

${mypi} = $(cat mypi)
scp piservo.py ${mypi}:~/dev/piservo
ssh ${mypi} 'cd ~/dev/piservo;sudo python piservo.py'
