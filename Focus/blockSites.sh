#!/bin/bash

for site in $BLOCK_SITES; do
  if ! grep -q "$site" /etc/hosts; then
    echo "127.0.0.1 $site" | sudo tee -a /etc/hosts
  fi
done
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
echo "Websites blocked."
