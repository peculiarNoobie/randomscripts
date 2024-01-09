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

# Hash the file contents using SHA-256
hash=$(sha256sum "$1" | cut -d " " -f 1)

echo "The SHA-256 hash of $1 is: $hash"
