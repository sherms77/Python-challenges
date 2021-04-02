'''
RULES
Invalid input: constraints: 1 <= n <= 100
Rule 1: if n is odd print Weird
Rule 2: if n is even and in the inlcusive range of 2 to 5 print Not Weird
Rule 3: if n is even and in the inclusive range of 6 to 20 print Weird
Rule 4: if n is even and greater than 20 print Not Weird
'''

# 020421: submitted this code in hr, it passed the test cases but failed 1/8 test cases when submitted.
# 020421: refer to screenshot failed sub_010421.png.

import math, os, random, re, sys

if __name__ == '__main__':
    n = int(input().strip())
    
    # Rule 4: if n is even and greater than 20 print Not Weird
    if n > 20 and n%2 == 0:
        print('Not Weird')

    # Rule 1: if n is odd print Weird
    elif n != n%2:
        print('Weird')
    
    # Rule 2: if n is even and in the inlcusive range of 2 to 5 print Not Weird
    elif n%2 in range (2,6):
        print('Not Weird')

    # Rule 3: if n is even and in the inclusive range of 6 to 20 print Weird
    elif n%2 in range (7,20):
        print('Not Weird')
    
    


    


