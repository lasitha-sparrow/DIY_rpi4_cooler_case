#!/bin/bash
# This is to set raspberry pi into monitoring mode
iw phy `iw dev wlan0 info | gawk '/wiphy/ {printf "phy" $2}'` interface add mon0 type monitor
echo "creating monitor interface"
sleep 3
ifconfig mon0 up
echo "Activate interface mon0"
sleep 3
echo "........................sucess........................!"
bettercap -iface mon0
