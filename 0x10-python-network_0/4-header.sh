#!/bin/bash
# takes in URL, sends GET request, displays body of response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
