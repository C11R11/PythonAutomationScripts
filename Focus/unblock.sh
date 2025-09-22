#!/bin/bash

for site in $BLOCK_SITES; do
  sudo sed -i '' "/$site/d" /etc/hosts
done
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
