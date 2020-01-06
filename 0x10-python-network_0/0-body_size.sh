#!/bin/bash
# takes in URL, sends request to that URL, displays size of body of response
curl -sI "$1" | grep Content-Length | cut -d ' ' -f 2
