# wrapped in function to test multliple test cases

import math, os, random, re, sys

def evenOdd (n):
   
    # Rule 4: if n is even and greater than 20 print Not Weird
    if n > 20 and n%2 == 0:
        print('Not Weird')

    # Rule 1: if n is odd print Weird
    elif n%2 != 0:
        print('Weird')
    
    # Rule 2: if n is even and in the inlcusive range of 2 to 5 print Not Weird
    elif n%2 == 0 and n in range (2,6):
        print('Not Weird')

    # Rule 3: if n is even and in the inclusive range of 6 to 20 print Weird
    elif n%2 == 0 and n in range (6,20): # elif n%2 in range (7,20):
        print('Not Weird')

'''
# rule 1
evenOdd(3) # out[3]: Weird - Correct
evenOdd(1) # out[1]: Weird - Correct
evenOdd(5) # out[5]: Weird  - Correct

090421: NEED TO TEST THIS BLOCK FOR RULE 1
evenOdd(7) # out[7]: Weird
evenOdd(9) # out[9]: Weird
evenOdd(11) # out[11]: Weird
evenOdd(13) # out[13]: Weird
evenOdd(15) # out[15]: Weird
evenOdd(17) # out[17]: Weird
evenOdd(19) # out[19]: Weird
'''

'''
# rule 2
evenOdd(2) # out[2]: Not Weird - Correct
evenOdd(4) # out[4]: Not Weird - Correct
'''

'''
# rule 3
# the number 6 is not included in rules 2 or 3 but should be included in 3. modified to include 6.
evenOdd(6) # out[6]: Not Weird 
evenOdd(8) # out[8]: Not Weird
evenOdd(10) # out[10]: Not Weird
evenOdd(12) # out[12]: Not Weird
evenOdd(14) # out[14]: Not Weird
evenOdd(16) # out[16]: Not Weird
evenOdd(18) # out[18]: Not Weird
evenOdd(20) # out[20]: Not Weird

# 090421: Tested outputs for rule 3 - ALL CORRECT
'''

# rule 4
evenOdd(24) # out[24]: Not Weird
evenOdd(100) # out[100]: Not Weird


