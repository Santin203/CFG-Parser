# CFG Parser

This project, developed for the Theory of Automata course (CS-3383) at Texas Tech University, delves into the exploration of Context-Free Grammars (CFGs) and their profound implications in language theory. CFGs, surpassing Regular Expressions in expressive power, form the backbone of compiler design and software development. The project empowers students to replicate established grammars in JFLAP, a tool used for theoretical machine exploration, and to craft their own programming language syntax.

## Grammars
The project encompasses three grammars:

HTML Grammar: This grammar represents a subset of HTML tags, crucial for web content rendering.

XML Grammar: Defining configuration files and facilitating data exchange on the web, XML grammar offers flexibility in tag definitions.

Custom Language Grammar: Simple custom syntax for a imaginary programming languague, incorporating diverse features such as if-else statements, loops, mathematical operations, function definitions, recursion, switch statements, print statements, and variable assignments.

The grammars are stored in .jff format compatible with JFLAP and are later converted to Chomsky Normal Form (CNF) for parsing using a CYK algorithm in Python.

## CFG to CNF Conversion
To facilitate parsing using the CYK algorithm, the grammars undergo conversion to Chomsky Normal Form. This conversion ensures uniformity and compatibility with the parsing algorithm.

## CYK Algorithm Implementation
The CYK algorithm implementation in Python reads grammars in CNF format and input strings from input.txt. It parses the input strings according to the selected grammar, enabling validation against the defined language structure.

## File Structure
grammar_html.txt: Grammar for HTML in CNF format.
grammar_xml.txt: Grammar for XML in CNF format.
grammar_custom.txt: Grammar for the custom programming language in CNF format.
input.txt: Input file containing strings to be parsed.
main.py: Python script implementing the CLI for the CYK algorithm for parsing.
