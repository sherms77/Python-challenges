# refactored code given by someone by fb user from Amigoscode

import math, os, random, re, sys

'''
240321:
# don't know how to execute code in vs code
# guessing I have to wrap in a function
# will just run the code as is in HR

# ran in HR - works

# NEXT STEP: Understand and explain code.
'''

even_condition1= [i for i in range(2,6)] # range will stop at 5
even_condition2= [i for i in range(6,21)]
if __name__ == '__main__':
    n = int(input().strip())

    if n%2 == 0 and n > 20:
        print('Not Weird')
    elif n%2 == 0 and n in even_condition1:
        print('Not Weird')
    elif n%2 == 0 and n in even_condition2:
        print('Weird')
    else:
        print('Weird')