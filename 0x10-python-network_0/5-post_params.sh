#!/bin/bash
# Takes a URL, sends a POST request and displays the body of the response
curl -sX POST "email=test@gmail.com" "subject=I will always be here for PLD" $1
