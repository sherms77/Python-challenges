# Rule 2: if n is even and in the inlcusive range of 2 to 5 print Not Weird

# n = int(input('Enter num:'))

def rule2(n):
    if n%2 in range(2,6):
        print('Not Weird')
    else:
        print('Weird')

rule2(2) # out[2]: Not Weird 
rule2(3) # out[3]: Weird
rule2(4) # out[4]: Not Weird
rule2(5) # out[5]: Weird

# 060421: INCORRECT OUTPUTS - ALL 'Weird'


