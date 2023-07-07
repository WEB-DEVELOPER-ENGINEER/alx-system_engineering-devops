#!/bin/bash
# Send custom headers to servers
curl -s -H "X-School-User-Id: 98" "$1"
