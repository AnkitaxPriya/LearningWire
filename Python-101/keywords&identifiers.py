# Keywords are the reserved words in Python 
# We cannot use a keyword as variable name, function or any other identifier
# Keywords are case sensitive


# Get all keywords in python 3.9

import keyword

print(keyword.kwlist)

print("\n Total number of keywords: ", len(keyword.kwlist))

"""
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

 Total number of keywords:  36
"""



# Identifiers
"""
Identifier is the name given to entities like class, functions, variables, etc in Python. It helps differentiating one entity from another.

Rules: 
1. Can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0-9) or an underscore(_)
2. Cannot start with a digit. 
3. Keywords can't be used as identifiers
4. Cannot use special sybols like !,@,#,$,% etc.
"""

12abc = 12
global = 1
a@ = 10

# SyntaxError: invalid syntax

