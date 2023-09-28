#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sX OPTIONS -i $1
