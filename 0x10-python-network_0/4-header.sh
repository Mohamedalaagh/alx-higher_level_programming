#!/bin/bash
# Script which takes a URL as an argument, sends a GET request to the URL, and displays the body of the response, A header variable X-HolbertonSchool-User-Id must be sent with 
curl -sHX "X-School-User-Id: 98" "$1"
