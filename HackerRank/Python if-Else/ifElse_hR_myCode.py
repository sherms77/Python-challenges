import math, os, random, re, sys

# Invalid input: constraints: 1 <= n <= 100
def invalid(v):
    if v <= 1 or v >= 100:
        print('invalid input')
    else:
        print('valid')

# invalid(700) # works - out[700]: invalid input
# invalid(10) # works - out[10]: valid

# Rule 1: if n is odd print Weird
def rule_one(w):
    even = w%2
    if even != 0:
        print('Weird')
    else:
        print('Even number')

# rule_one(3) # works - out[3]: Weird
# rule_one(6) # works - out[7]: Even number

# Rule 2: if n is even and in the inlcusive range of 2 to 5 print Not Weird
def rule_two(x):
    if x in range(2,5) and (x%2) == 0:
        print('Not Weird')
    else:
        print('Outside of range')

# rule_two(2) # works - out[2]: Not weird
# rule_two(4) # works - out[2]: Not weird
# rule_two(10) # works - out[10]: Outside of range
# rule_two(3) # works - out[3]: Outside of range

# Rule 3: if n is even and in the inclusive range of 6 to 20 print Weird
def rule_three(y):
    if y in range(6,20) and (y%2) == 0:
        print('Weird')
    else:
        print('Outside of range')

# rule_three(10) # works - out[10]: Weird
# rule_three(7) # works - out[7]: Outside of range
# rule_three(3) # works - out[3]: Outside of range
# rule_three(84) # works - out[84]: Outside of range

# Rule 4: if n is even and greater than 20 print Not Weird
def rule_four(z):
    if z > 20 and (z%2) == 0:
        print('Not Weird')
    else:
        print('Number is less than 20 or odd')

rule_four(21) # works - out[21]: Number is less than 20 or odd
rule_four(22) # works - out[22]: Weird
rule_four(7) # works - out[7]: Number is less than 20 or odd

'''
def main(n):
    # might create new file and put all functions into one function.
    # arguments need to pass different rules for correct output.

    # invalid(n)
    # rule_one(n)
    
# main(3) # [out]: 'invalid input'
# main(3) # [out]: 'Not Weird'

# rule_one(3) # [out]: blank
# rule_one(200) # [out]: 'Invalid input'
'''