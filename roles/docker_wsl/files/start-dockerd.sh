#!/bin/bash

if ! pgrep -f '^dockerd$' > /dev/null; then
  nohup sudo -b dockerd < /dev/null > /var/log/docker/dockerd.log 2>&1
fi
