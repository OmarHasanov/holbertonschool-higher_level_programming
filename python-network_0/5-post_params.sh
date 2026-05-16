#!/bin/bash
# Sends a POST request with specific data parameters to a URL
curl -s -d "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"
