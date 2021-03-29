# refactored code given by someone by fb user from Amigoscode
import math, os, random, re, sys

'''
240321:
# don't know how to execute code in vs code
# guessing I have to wrap in a function
# will just run the code as is in HR

# ran in HR - works.

# NEXT STEP: Understand and explain code.
'''

# 290321: no rule for constraint?
# 290321: i think the constraint rule is applied through the ranges in lines 24 and 26

if __name__ == '__main__':
    num = int(input().strip())

    if num % 2 != 0:
        print("Weird")
    else:
        if num >= 2 and num <= 5:
            print("Not Weird")
        elif num <= 20:
            print("Weird")
        else: 
            print("Not Weird")

