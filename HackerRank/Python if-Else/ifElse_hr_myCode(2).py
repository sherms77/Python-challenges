# step 6 | method 2
import math, os, random, re, sys

def main_combined(a):
    even = a%2

    # invalid input_constraint: 1 <= n <= 100
    # no output if input valid
    if a <= 1 or a >= 100:
        print('Invalid input')
    
    # Rule 1: if n is odd print Weird
    if even != 0:
        print('Weird')
    else:
        print('Even number')

    # 170321: I NEED IT TO BREAK OUT OF FUNCTION IF IT MEETS ONE RULE?
    # 170321: DRAW FLOW CHART.
    # 170321: GO OVER PROBLEM SPEC AND INTENDED OUTPUT AGAIN. 
    # 170321: ONE ARGUMENT CAN MEET MORE THAN ONE RULE.

    # Rule 2: if n is even and in the inlcusive range of 2 to 5 print Not Weird
    if a in range(2,5) and even == 0: # (a%2) == 0: - replaced with even variable
        print('Not Weird')
    else:
        print('Outside of range')

    # Rule 3: if n is even and in the inclusive range of 6 to 20 print Weird
    if a in range(6,20) and even == 0: # (y%2) == 0: - replaced with even variable
        print('Weird')
    else:
        print('Outside of range')

    # Rule 4: if n is even and greater than 20 print Not Weird
    if a > 20 and (a%2) == 0:
        print('Not Weird')
    else:
        print('Number is less than 20 or odd')

main_combined(3) # 160321: DOES NOT WORK AS INTENDED. CHECKS AGAINST EACH RULE AND GIVES RELEVANT OUTPUT - out[3]: Weird
# main_combined(24) # out[24]: Not weird
