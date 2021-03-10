import math, os, random, re, sys

def invalid(v):
    if v <= 1 or v >= 100:
        print('invalid input')
    else:
        print('valid')

# invalid(700) # works - out[700]: invalid input
# invalid(10) # works - out[10]: valid

# RULE_ONE DOES NOT WORK | Refer to comment on line 20.
def rule_one(w):
    if w != w%2:
        print('Weird')
    else:
        print('This is an even number.')

rule_one(6) # works - out[6]: Weird
rule_one(7) # DOES NOT WORK: outputs Weird | SHOULD BE: out[7]: This is an even number.

def rule_two(x):
    if x in range(2,5) and (x%2) == 0:
        print('Not Weird')
    else:
        print('outside of range')

def rule_three(y):
    pass

def rule_four(z):
    pass
 
def main(n):
    invalid(n)
    rule_one(n)
    
# main(3) # [out]: 'invalid input'
# main(3) # [out]: 'Not Weird'

# rule_one(3) # [out]: blank
# rule_one(200) # [out]: 'Invalid input'
