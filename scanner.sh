#!/bin/bash
echo "enter IP address: "
read ip
echo "enter NSE script name: "
read script
echo "running scan on $ip with script $script..."
nmap --script=$script $ip