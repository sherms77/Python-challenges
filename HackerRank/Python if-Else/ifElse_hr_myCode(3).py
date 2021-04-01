# step 6 | method 2
import math, os, random, re, sys

def main_combined(a):
    even = a%2

    # Invalid input: constraints: 1 <= n <= 100
    # 310321: Still need to try and get range rule correct
    # 310321: Refer to fb users comments about my range for invalid input rule (both fb users)
    if a > 1 and a < 100:
        print('Invalid input')

    elif even != 0:
        print('Weird')

    elif a in range(2,5) and even == 0:
        print('Not Weird')

    elif a in range(6,20) and even == 0:
        print('Weird')

    elif a > 20 and (a%2) == 0:
        print('Not Weird')
    
main_combined(3) # out[3]: Weird - DOES NOT WORK OUT: Invalid input
'''
main_combined(24) # out[24]: Not weird
main_combined(1) # out[1]: Invalid input
main_combined(100) # out[100]: Invalid input
'''