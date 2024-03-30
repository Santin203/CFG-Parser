# This program takes an XML/HTML file as input and generates a text file that can be used as input to the main program.
# It removes all the spaces and newlines, and puts everything in lowercase.
# Output file is saved in the same directory as the input file.
import re
import os

def remove_spaces(text):
    return text.replace(' ', '')

def remove_newlines(text):
    return re.sub(r'\n+', ' ', text)

def lower(text):
    return text.lower()

def generate_input_file(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    text = remove_newlines(text)
    text = remove_spaces(text)
    text = lower(text)
    with open(output_file, 'w') as f:
        f.write(text)

def main():
    input_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name = input("Enter the name of the XML/HTML file: ")
    input_file_path = os.path.join(input_file_path, file_name)
    output_file = os.path.join(os.path.dirname(input_file_path), 'input.txt')
    
    try:
        generate_input_file(input_file_path, output_file)
    except:
        print("Error: File not found.")
        return

main()
print("Input file generated successfully!")