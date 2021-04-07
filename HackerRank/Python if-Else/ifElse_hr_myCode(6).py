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
    elif n%2 and n in range (2,6):
        print('Not Weird')

    # Rule 3: if n is even and in the inclusive range of 6 to 20 print Weird
    elif n%2 and n in range (6,20): # elif n%2 in range (7,20):
        print('Not Weird')
'''
# rule 1
evenOdd(3) # out[3]: Weird - Correct
evenOdd(1) # out[1]: Weird - Correct
'''

# rule 2
# GOT ONE OUTPUT OF WEIRD. INCORRECT. NEED TO DEBUG TO SEE WHAT IS GOING ON.
evenOdd(2) # out[2]: Not Weird
evenOdd(4) # out[4]: Not Weird
evenOdd(5) # out[5]: Not Weird

'''
# rule 3
# out[rule 3]: Not Weird
evenOdd(6) # 6 is not included in rules 2 or 3 but should be included in 3. modified to include 6.
evenOdd(7)
evenOdd(8)
evenOdd(9)
evenOdd(10)
evenOdd(11)
evenOdd(12)
evenOdd(13)
evenOdd(14)
evenOdd(15)
evenOdd(16)
evenOdd(17)
evenOdd(18)
evenOdd(19)
evenOdd(20)

# rule 4
evenOdd(24) # out[24]: Not Weird
evenOdd(100) # out[100]: Not Weird
'''