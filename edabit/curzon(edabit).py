# Curzon challenge from edabit.com

'''
In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
'''

def is_curzon(n):
    r1 = (1+2)**n
    return r1
    r2 = (1+2)*n
    return r2
    if r1 / r2 != %:
        return True
    else:
        return False

is_curzon(5)
