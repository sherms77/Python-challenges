# How to think like a cs Pg.75
# Abecedarian example - concatenation and for loop

prefixes = 'JKLMNOPQ'
suffix = 'ack'
extended = 'uack'

for letter in prefixes:
    if letter == 'O': 
        print(letter + extended) # if letter is 'O' concatenate with extended
    elif letter == 'Q': 
        print(letter + extended) # else if letter is 'Q' concatenate with extended
    else: 
        print(letter + suffix) # else concatenate with suffix