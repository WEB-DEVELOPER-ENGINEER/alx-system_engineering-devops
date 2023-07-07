#!/bin/bash
# Get the allowed methods in a server
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
