#!/bin/bash
# Get the comtent-lenght of the giving ip address
curl -sI "$1" | awk '/Content-Length/{print $2}'
