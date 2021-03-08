import math, os, random, re, sys

def invalid(x):
    if x <= 1 or x >= 100:
        print('invalid input')
    
def rule_one(y):
    if y in range(2,5) and (y % 2) == 0:
        print('Not Weird')
    else:
        print('outside of range')

def rule_two(j):
    pass

def rule_three(k):
    pass
 
def main(n):
    invalid(n)
    rule_one(n)
    
main(200) # [out]: 'invalid input'
# main(3) # [out]: 'Not Weird'

# rule_one(3) # [out]: blank
# rule_one(200) # [out]: 'Invalid input'

'''
# hackerRank code
import math, os, random, re, sys

if__name__ == '__main__':
    n = int(input().strip())
'''
