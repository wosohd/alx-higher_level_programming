#!/bin/bash
# takes URL sends request to it and display size of body respose
curl -s "$1" | wc -c
