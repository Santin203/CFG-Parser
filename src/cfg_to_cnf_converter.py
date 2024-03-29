def eliminate_unit_productions(grammar):
    unit_free_grammar = {}
    for non_terminal, productions in grammar.items():
        unit_free_productions = set()
        for production in productions:
            if len(production) == 1 and production[0] in grammar:
                unit_free_productions |= eliminate_unit_productions({production[0]: grammar[production[0]]})
            else:
                unit_free_productions.add(production)
        unit_free_grammar[non_terminal] = unit_free_productions
    return unit_free_grammar

def eliminate_epsilon_productions(grammar):
    nullable = set()
    for non_terminal, productions in grammar.items():
        if '' in productions:
            nullable.add(non_terminal)
    epsilon_free_grammar = {}
    for non_terminal, productions in grammar.items():
        epsilon_free_productions = set()
        for production in productions:
            if production:
                for i in range(len(production)):
                    if production[i] in nullable:
                        new_production = production[:i] + production[i+1:]
                        epsilon_free_productions.add(new_production)
        epsilon_free_grammar[non_terminal] = epsilon_free_productions
    return epsilon_free_grammar

def convert_to_cnf(grammar):
    cnf_grammar = {}
    unit_free_grammar = eliminate_unit_productions(grammar)
    epsilon_free_grammar = eliminate_epsilon_productions(unit_free_grammar)
    non_terminals = set(grammar.keys())
    
    for non_terminal, productions in epsilon_free_grammar.items():
        for production in productions:
            if len(production) > 2:
                for i in range(len(production) - 2):
                    new_non_terminal = f'CNF_{len(cnf_grammar)}'
                    cnf_grammar[new_non_terminal] = {(production[i], production[i+1])}
                    non_terminals.add(new_non_terminal)
                    production = production.replace(production[i:i+2], new_non_terminal, 1)
        if non_terminal not in cnf_grammar:
            cnf_grammar[non_terminal] = productions

    for non_terminal, productions in cnf_grammar.items():
        for production in productions:
            if len(production) > 2:
                new_non_terminal = f'CNF_{len(cnf_grammar)}'
                cnf_grammar[new_non_terminal] = {(production[:-1],)}
                non_terminals.add(new_non_terminal)
                production = production.replace(production[:-1], new_non_terminal, 1)
                
    return cnf_grammar

def print_grammar(grammar):
    for non_terminal, productions in grammar.items():
        for production in productions:
            print(f"{non_terminal} -> {' '.join(production)}")

# Example CFG
cfg = {
    'X': {('E',)},
    'E': {('<htmlR>', 'C', '</html>')},
    'R': {('$',), ('lang="C"',)},
    'C': {('E',), ('Z',)},
    'T': {('n',), ('$')},
    'Z': {('T', 'Z'), ('$')}
}

cnf_grammar = convert_to_cnf(cfg)
print_grammar(cnf_grammar)
