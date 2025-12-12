#!/usr/bin/env python3
import argparse
import re
import sys
import os

def filter_text(input_path, output_path):
    """
    Reads text from input_path, replaces all instances of the word 'god' (case-insensitive)
    with 'koko', and writes the result to output_path.
    """
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)

    try:
        # Regex for case-insensitive 'god' surrounded by word boundaries
        # Using word boundaries (\b) ensures we match the word "god" and not inside "godmother"
        pattern = re.compile(r'\bgod\b', re.IGNORECASE)
        
        with open(input_path, 'r', encoding='utf-8') as fin, \
             open(output_path, 'w', encoding='utf-8') as fout:
            for line in fin:
                fout.write(pattern.sub('koko', line))
            
        print(f"Successfully processed '{input_path}' and saved to '{output_path}'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter novel text by replacing 'god' with 'koko'.")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("output_file", help="Path to the output text file")
    
    args = parser.parse_args()
    
    filter_text(args.input_file, args.output_file)
