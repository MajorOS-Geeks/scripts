#! /bin/bash

case $1 in 
	on)
	if [[ -f /etc/modprobe.d/usb_block.conf ]]
	then
		sudo mv /etc/modprobe.d/usb_block.conf /etc/modprobe.d/usb_block.conf.backup
	else
		echo "USB storage is already on"
		

	fi
	;;
	off)
	if [[ -f /etc/modprobe.d/usb_block.conf.backup ]]
	then
		sudo mv /etc/modprobe.d/usb_block.conf.backup /etc/modprobe.d/usb_block.conf
	else
		echo "USB storage is already turned off"
	fi
	;;
	*)
		echo "Press -h for help"
	;;
esac
