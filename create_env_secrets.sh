#!/bin/bash

# File containing secret variable names, one per line
VARS_FILE="vars.txt"

# Output .env file
ENV_FILE="app/.env"

# Ensure .env file exists
touch "$ENV_FILE"

# Write each secret variable to .env file
while IFS= read -r secret_name; do
    secret_value=$(echo "${{ secrets.$secret_name }}")
    echo "$secret_name=$secret_value" >> "$ENV_FILE"
done < "$VARS_FILE"

echo "Secret variables written to $ENV_FILE"