#!/bin/bash

# Script to generate CSS @font-face rules for .ttf files in the current directory

# File where the font-face rules will be stored
output_file="font_face.txt"

# Check if the output file already exists, if so, remove it to start fresh
if [ -f "$output_file" ]; then
	rm "$output_file"
fi

# Loop through all .ttf files in the current directory
for font_file in *.ttf; do
	# Extract the font name from the file name (remove the extension .ttf)
	font_name="${font_file%.ttf}"

	# Generate the @font-face rule
	echo "@font-face {" >>"$output_file"
	echo "  font-family: \" \";" >>"$output_file"
	echo "  src: url(\"generated_fonts/$font_file\") format(\"truetype\");" >>"$output_file"
	echo "}" >>"$output_file"
	echo "" >>"$output_file" # Add a blank line for readability
done

echo "Font face rules generated in $output_file."
