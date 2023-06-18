#!/bin/bash

sleep 15 # Wait for InfluxDB to start

# Create user
influx user create -n Administrator1 -p Administrator1 -o samsung

# Generate API token
API_TOKEN=$(influx auth create -n Administrator1 -o samsung-p --hide-headers | awk '{print $3}')

echo "InfluxDB initialization complete"
echo "API Token: $API_TOKEN"
