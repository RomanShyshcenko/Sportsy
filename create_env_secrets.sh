#!/bin/bash

# Check for required files
if [ ! -f "vars.txt" ]; then
  echo "Error: vars.txt file not found."
  exit 1
fi

# Create the .env file
touch .env

# Read each variable name from the vars.txt file
while IFS= read -r var_name; do
  # Check if the secret exists in GitHub Actions
  if [[ -z "${!var_name}" ]]; then
    echo "Warning: Secret ${var_name} not found in GitHub Actions."
  else
    # Write the variable to the .env file
    echo "${var_name}=${!var_name}" >> .env
  fi
done < "vars.txt"