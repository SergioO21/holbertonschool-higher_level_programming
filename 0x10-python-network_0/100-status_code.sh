#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sIo /dev/null --write-out '%{http_code}\n' "$1"
