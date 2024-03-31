import pytest
from src.main import *
from src.xml_to_input_format import *
#from main import *

def test_accept_CYK():
    # Test case 0: w is not epsilon and G is a CFG in CNF for simple operations precedence
    G = {
        'E': ['EL', 'EK', 'XJ', 'n', 'TI', 'TH'],
        'L': ['BT'],
        'B': ['+'],
        'K': ['CT'],
        'C': ['-'],
        'T': ['n', 'XJ', 'TI', 'TH'],
        'F': ['n', 'XJ'],
        'X': ['n'],
        'J': ['GF'],
        'G': ['^'],
        'I': ['DF'],
        'D': ['/'],
        'H': ['AF'],
        'A': ['*']
    }
    assert accept_CYK('n+n*n^n', G, 'E') == True
    
    assert accept_CYK('n+', G, 'E') == False
    
    assert accept_CYK('n+n', G, 'E') == True
    
    # Test case 1: w is epsilon and S is in G
    G = {'S': ['$']}
    assert accept_CYK('$', G, 'S') == True

    # Test case 2: w is not epsilon and S is not in G
    G = {'A': ['a']}
    assert accept_CYK('b', G, 'S') == False

    # Test case 3: w is not epsilon and S is in G
    G = {'S': ['AB'], 'A': ['a'], 'B': ['b']}
    assert accept_CYK('ab', G, 'S') == True

    # Test case 4: w is not epsilon and S is not in G
    G = {'S': ['AB', 'BC'], 'A': ['a'], 'B': ['b'], 'C': ['c']}
    assert accept_CYK('abc', G, 'D') == False

    # Test case 5: w is not epsilon and S is in G with multiple derivations
    G = {'S': ['AB', 'BC'], 'A': ['a'], 'B': ['b'], 'C': ['c']}
    assert accept_CYK('ab', G, 'S') == True

    # Test case 6: w is not epsilon and S is in G with multiple derivations
    G = {'S': ['AB', 'BC'], 'A': ['a'], 'B': ['b'], 'C': ['c']}
    assert accept_CYK('bc', G, 'S') == True
    
    G = read_grammar('./grammar_custom.txt')
    W = read_input('./custom_test1.txt')
    assert accept_CYK(W, G, 'X') == True
    
    W = read_input('./custom_test2.txt')
    assert accept_CYK(W, G, 'X') == True
    
    W = read_input('./custom_test3.txt')
    assert accept_CYK(W, G, 'X') == True
    
    W = read_input('./custom_test4.txt')
    assert accept_CYK(W, G, 'X') == True
    
    W = read_input('./custom_test5.txt')
    assert accept_CYK(W, G, 'X') == True
    
    W = read_input('./custom_test6.txt')
    assert accept_CYK(W, G, 'X') == True
    
    W = read_input('./custom_test7.txt')
    assert accept_CYK(W, G, 'X') == True
    
    W = read_input('./custom_test8.txt')
    assert accept_CYK(W, G, 'X') == True
    
    W = read_input('./custom_test9.txt')
    assert accept_CYK(W, G, 'X') == True
    
    G = read_grammar('./grammar_xml.txt')
    conversion_to_input_format('./xml_test1.xml')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./xml_test2.xml')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./xml_test3.xml')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    G = read_grammar('./grammar_html.txt')
    conversion_to_input_format('./html_test1.html')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./html_test2.html')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./html_test3.html')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./html_test4.html')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./html_test5.html')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./html_test6.html')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./html_test7.html')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    
    conversion_to_input_format('./html_test8.html')
    W = read_input('./input.txt')
    assert accept_CYK(W, G, 'X') == True
    