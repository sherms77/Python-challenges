# step 6 | method 2
import math, os, random, re, sys

def main_combined(a):
    even = a%2

    # constraint: 1 <= n <= 100 | no output if input invalid
    if a <= 1 or a >= 100:
        print('Invalid input')
    
    # Rule 1: if n is odd print Weird
    elif even != 0:
        print('Weird')

    # Rule 2: if n is even and in the inlcusive range of 2 to 5 print Not Weird
    elif a in range(2,5) and even == 0: 
        print('Not Weird')
    
    # Rule 3: if n is even and in the inclusive range of 6 to 20 print Weird
    elif a in range(6,20) and even == 0:
        print('Weird')
    
    # Rule 4: if n is even and greater than 20 print Not Weird
    elif a > 20 and (a%2) == 0:
        print('Not Weird')
    
# main_combined(3) # works - out[3]: Weird
main_combined(24) # works - out[24]: Not weird