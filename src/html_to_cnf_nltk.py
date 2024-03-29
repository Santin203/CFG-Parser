# INput .jff file, output CNF grammar in nltk format

from nltk import CFG

grammar = CFG.fromstring("""
X -> E
E -> A F D C A B F D
C -> E
C -> Z
T -> 'n'
T -> ''
Z -> TZ
Z -> ''
A -> '<'
B -> '/'
D -> '>'
F -> 'html'
""")
#print(grammar)
c = grammar.chomsky_normal_form()
print(c._productions)

# Open the output file
with open('grammar.txt', 'w') as f:
    # Iterate over all keys (non-terminals) in the dictionary
    for production in c._productions:
        # Write the production to the file
        f.write(f'{production}\n')

