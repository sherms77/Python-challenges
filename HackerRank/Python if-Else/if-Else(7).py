import math, os, random, re, sys

n = int(input('enter a number: '))

if n >= 1 and n <=100: # constraint: 1 <= n <= 100 - statements below encapsulated in constraint, must meet this condition to progress.
    if n%2: # if n is odd print Weird - you don't have to put != 0 here because it divides n with 2 to produce 0 remainder. It the remainder is 0 it will print Weird.
        print('Weird')
    elif n%2 == 0 and n >=2 and n <=5: # if n is even and between inclusive range 2 to 5 print Not Weird
        print('Not Weird')
    elif n%2 == 0 and n >=6 and n <=20: # if n is even and between inclusive range 6 to 20 print Weird
        print('Weird')
    elif n%2 == 0 and n >20: # if n is even and greater than 20 print Not Weird
        print('Not Weird')
else:
    print('Number outside of range')
   
'''
TEST - MODULO OPERATOR
if n%2 and n > 2: # n%2 means the remainder will be 0 (for an even number) so n will become 0 and will never be greater than 2.
        print('the test works')
'''

