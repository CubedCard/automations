#!/bin/bash

if ! command -v ffmpeg &> /dev/null; then
    echo "FFmpeg is not installed. Please install it first."
    exit 1
fi

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file.mov>"
    exit 1
fi

input_file="$1"
output_file="${input_file%.*}.mp4"

ffmpeg -i "$input_file" -c:v libx264 -c:a aac -strict experimental "$output_file"

if [ $? -eq 0 ]; then
    echo "Conversion successful: $output_file"
else
    echo "Conversion failed."
    exit 1
fi

