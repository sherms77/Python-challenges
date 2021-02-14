# function that stutters words

def stutter(word):
    return word[:2]+ '... ' +word[:2]+ '... ' +word+ '?' # works
    
print(stutter('incredible'))
print(stutter('enthusiastic'))
    
