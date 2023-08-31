#!/bin/bash
# takes URL, sends GET requets for it and displays the body of response

curl -sH "X-School-User-Id: 98" "$1"
