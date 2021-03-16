# step 6 | method 2
import math, os, random, re, sys

def main_combined(a):
    even = a%2

    # invalid input_constraint: 1 <= n <= 100
    if a <= 1 or a >= 100:
        print('Invalid input')
    else:
        print('Valid')

    # Rule 1: if n is odd print Weird
    # even = a%2
    if even != 0:
        print('Weird')
    else:
        print('Even number')

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

# 160321: UP TO RULE 4

# Rule 4: if n is even and greater than 20 print Not Weird
def rule_four(z):
    if z > 20 and (z%2) == 0:
        print('Not Weird')
    else:
        print('Number is less than 20 or odd')

# rule_four(21) # works - out[21]: Number is less than 20 or odd
# rule_four(22) # works - out[22]: Weird
# rule_four(7) # works - out[7]: Number is less than 20 or odd

# Combine functions into one function
# Method 1: Call each function in main function
def main(n):
    # 160321: i don't think this will work bc the argument will get passed to each function and the operation will be performed accordingly.
    invalid(n)
    rule_one(n)
    rule_two(n)
    rule_three(n)
    rule_four(n)

main(3) # DOES NOT WORK AS INTENDED - out[3]: Weird
# 160321: As above, the argument is processed by each function and relevant output given.
# 160321: Need to make conditional so only one output is given.
# 160321: Will try method 2.
