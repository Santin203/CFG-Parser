# This script reads a context-free grammar in XML format and converts it to a dictionary that represents the grammar in Chomsky Normal Form (CNF).
# It writes the grammar to a file in the format required by the CYK algorithm.
import xml.etree.ElementTree as ET
import os

# The path to your XML file
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xml_cnf.jff')

# Parse the XML file
try:
    tree = ET.parse(file_path)
except:
    print("Error: File not found.")
    exit()
    
root = tree.getroot()

# Initialize the dictionary for the rules of the grammar
R = {}

# Iterate over all 'production' elements in the XML
for production in root.iter('production'):
    # Get the non-terminal and the right-hand side of the production
    non_terminal = production.find('left').text
    rhs = production.find('right').text

    # If the non-terminal is not in the dictionary yet, add it
    if non_terminal not in R:
        R[non_terminal] = []

    try: 
        # Add the right-hand side of the production to the list of rules for the non-terminal
        R[non_terminal].append(rhs.split())  # Change this line
    except:
        # Add the right-hand side of the production to the list of rules for the non-terminal
        # $ is epsilon
        R[non_terminal].append(["$"])

# Now, R is a dictionary that represents the grammar in the desired format
print("The grammar is: " + str(R))
print("The non-terminals are: " + str(list(R.keys())))

# Open the output file
with open('grammar.txt', 'w') as f:
    # Iterate over all keys (non-terminals) in the dictionary
    for non_terminal in R:
        # Get all the production rules for this non-terminal
        productions = R[non_terminal]
        
        # Iterate over all production rules
        for production in productions:
            # Write the production to the file
            f.write(f'{non_terminal} -> {" ".join(production)}\n')
