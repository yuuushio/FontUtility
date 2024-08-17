#!/bin/bash

# Define the strings to prepend and append
PREPEND="Livory-"
APPEND=".woff2"

cd livory/

# Loop through all files in the current directory
for file in *; do
    # Check if the file is not a Python script
    if [[ ! $file == *.py ]]; then
        # Extract the file extension
        extension="${file##*.}"
        filename="${file%.*}"

        # Rename the file
        mv "$file" "${PREPEND}${filename}${APPEND}"
    fi
done



