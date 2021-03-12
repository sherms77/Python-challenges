import math, os, random, re, sys

def invalid(v):
    if v <= 1 or v >= 100:
        print('invalid input')
    else:
        print('valid')

# invalid(700) # works - out[700]: invalid input
# invalid(10) # works - out[10]: valid

def rule_one(w):
    even = w%2
    if even != 0:
        print('Weird')
    else:
        print('Even number')

# rule_one(3) # works - out[3]: Weird
# rule_one(6) # works - out[7]: Even number

def rule_two(x):
    if x in range(2,5) and (x%2) == 0:
        print('Not Weird')
    else:
        print('Outside of range')

# rule_two(2) # works - out[2]: Not weird
# rule_two(4) # works - out[2]: Not weird
# rule_two(10) # works - out[10]: Outside of range
# rule_two(3) # works - out[3]: Outside of range

def rule_three(y):
    # Rule 3: if n is even and in the inclusive range of 6 to 20 print Weird
    pass

def rule_four(z):
    pass

def main(n):
    # might create new file and put all functions into one function.
    # arguments need to pass different rules for correct output.

    # invalid(n)
    # rule_one(n)
    
# main(3) # [out]: 'invalid input'
# main(3) # [out]: 'Not Weird'

# rule_one(3) # [out]: blank
# rule_one(200) # [out]: 'Invalid input'
