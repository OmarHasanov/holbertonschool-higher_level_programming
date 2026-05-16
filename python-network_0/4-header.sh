#!/bin/bash
# Sends a GET request with a specific header variable and value to a URL
curl -sH "X-School-User-Id: 98" "$1"
