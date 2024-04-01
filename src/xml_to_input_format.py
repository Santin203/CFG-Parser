# This program takes an XML/HTML file as input and generates a text file that can be used as input to the main program.
# It removes all the spaces and newlines, and puts everything in lowercase.
# Output file is saved in the same directory as the input file.

import re
import os

# removes all the spaces in the text
def remove_spaces_xml(text):
    return text.replace(' ', '')

# only removes the spaces that are not between the tags
def remove_spaces_html(text):
    return re.sub(r'(?<=>)\s+(?=<)', '', text)

# removes all the newlines in the text
def remove_newlines(text):
    return re.sub(r'\n+', ' ', text)

# changes all the letters to lowercase
def lower(text):
    return text.lower()

# function that changes the letters between the tags to "n", do not change the tags or the attributes
def change_letters(text):
    # change the letters inside "" to "n"
    new_text = re.sub(r'".*?"', r'"n"', text)
    
    return re.sub(r'>([^<]+)<', r'>n<', new_text)

# generates the input file in the format required by the main program
def generate_input_file_xml(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    text = remove_newlines(text)
    text = remove_spaces_xml(text)
    text = lower(text)
    with open(output_file, 'w') as f:
        f.write(text)

# generates the input file in the format required by the main program
def generate_input_file_html(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    text = remove_newlines(text)
    text = remove_spaces_html(text)
    text = lower(text)
    text = change_letters(text)
    with open(output_file, 'w') as f:
        f.write(text)

# function that calls the appropriate functions to generate the input file
def conversion_to_input_format(file_name):
    input_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file_path = os.path.join(input_file_path, file_name)
    output_file = os.path.join(os.path.dirname(input_file_path), 'input.txt')
    
    try:
        if file_name.endswith('.xml'):
            generate_input_file_xml(input_file_path, output_file)
        else:
            generate_input_file_html(input_file_path, output_file)
        print("Input file generated successfully!")
    except:
        print("Error: File not found.")
        return
    
def conversion_string_to_input_format_html(string):
    text = remove_newlines(string)
    text = remove_spaces_html(text)
    text = lower(text)
    text = change_letters(text)
    return text