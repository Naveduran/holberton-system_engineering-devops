#!/bin/bash
# request an URL and displays the size of the body of the response
curl "$1" -s -o A | cat A | wc -m
