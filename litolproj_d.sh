#!/bin/bash

# Check if a file path was provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

# Check if the file exists and is readable
if [ ! -r "$1" ]; then
  echo "Error: $1 is not a readable file"
  exit 2
fi

# Read the contents of the file
contents=$(cat "$1")

# Hash the file contents using SHA-256
hash=$(echo -n "$contents" | sha256sum | cut -d " " -f 1)

# Decode the hashed content using openssl
decoded=$(echo -n "$hash" | xxd -r -p | openssl enc -d -aes-256-cbc)

echo "The decoded content of $1 is: $decoded"