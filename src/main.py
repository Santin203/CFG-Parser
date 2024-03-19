# Program that takes as an input a CNF, runs CYK algorithm and returns if the input string is in the language of the grammar
# By Santiago Jiménez
# Python implementation for the
# CYK Algorithm

# Non-terminal symbols
# non_terminals = ["NP", "Nom", "Det", "AP", 
# 				"Adv", "A"]
# terminals = ["book", "orange", "man", 
# 			"tall", "heavy", 
# 			"very", "muscular"]

# # Rules of the grammar
# R = {
# 	"NP": [["Det", "Nom"]],
# 	"Nom": [["AP", "Nom"], ["book"], 
# 			["orange"], ["man"]],
# 	"AP": [["Adv", "A"], ["heavy"], 
# 			["orange"], ["tall"]],
# 	"Det": [["a"]],
# 	"Adv": [["very"], ["extremely"]],
# 	"A": [["heavy"], ["orange"], ["tall"], 
# 		["muscular"]]
# 	}
import xml.etree.ElementTree as ET


# The path to your XML file
file_path = r'C:\Users\Casas\OneDrive - Texas Tech University\Documents\Texas Tech\Spring 2024\CS-3383\Projects\Project 2\src\hw2_cnf.jff'

# Parse the XML file
tree = ET.parse(file_path)
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

    # Add the right-hand side of the production to the list of rules for the non-terminal
    R[non_terminal].append(list(rhs))

# Now, R is a dictionary that represents the grammar in the desired format

print("The grammar is: " + str(R))
print("The non-terminals are: " + str(R.keys()))




# Function to perform the CYK Algorithm
def cykParse(w):
	n = len(w)
	
	# Initialize the table
	T = [[set([]) for j in range(n)] for i in range(n)]

	# Filling in the table
	for j in range(0, n):

		# Iterate over the rules
		for lhs, rule in R.items():
			for rhs in rule:
				
				# If a terminal is found
				if len(rhs) == 1 and \
				rhs[0] == w[j]:
					T[j][j].add(lhs)

		for i in range(j, -1, -1): 
			
			# Iterate over the range i to j + 1 
			for k in range(i, j + 1):	 

				# Iterate over the rules
				for lhs, rule in R.items():
					for rhs in rule:
						
						# If a terminal is found
						if len(rhs) == 2 and \
						rhs[0] in T[i][k] and \
						rhs[1] in T[k + 1][j]:
							T[i][j].add(lhs)

	# If word can be formed by rules 
	# of given grammar
	if len(T[0][n-1]) != 0:
		print("True")
	else:
		print("False")
	
# Driver Code

# Given string
w = "n+n".split()

# Function Call
cykParse(w)
