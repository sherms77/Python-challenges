# refer to /home/sherms/HackerRank/Python/Python if-Else/README.txt
import math, os, random, re, sys

# invalid(x): constraint 1 <= n <= 100
# rule_two(y): if n is even and in the within the range of 2 to 5 print "Not Weird"

# NEXT STEP: Create rules 2 and 3
# ISSUE: main(200) gives two outputs: 'invalid input' and 'outside of range' - look into.

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
