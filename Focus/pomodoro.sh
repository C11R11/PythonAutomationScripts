#!/bin/bash

# Block websites
for site in $BLOCK_SITES; do
    if ! grep -q "$site" /etc/hosts; then
        echo "127.0.0.1 $site" | sudo tee -a /etc/hosts > /dev/null
    fi
done

sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
echo "Websites blocked for 1 hour."

# Wait for 1 hour (3600 seconds)
sleep 3600

# Unblock websites after timer
for site in $BLOCK_SITES; do
    sudo sed -i '' "/$site/d" /etc/hosts
done

sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
echo "Pomodoro complete: Websites unblocked."
