#! /bin/bash

# Check if at least one agrument is provided.
# This argument is the extension of the font file
if [ $# -eq 0 ]; then
	echo "No agruments provided. Provide file extension."
	exit 1
fi

# Loop through each argument (file)
for ext in "$@"; do
	# Find files with the given extension and extract the name
	for file in *.$ext; do
		# Check if file exists
		if [ -e "$file" ]; then
			# Extract the name before the extension and append to a .txt file
			echo "${file%.*}" >>fonts.txt
		fi
	done
done

echo "Name extraction complete. Check 'fonts.txt' for the list of font files."
