def element_from_set(s):
    return (s).pop()

print(element_from_set({'edabit'})) # returns '{'edabit'} but needs to return 'edabit'
print(element_from_set({True})) # True
print(element_from_set({(1, 2, 3)})) # (1, 2, 3))
print(element_from_set({11037})) # (11037)
print(element_from_set({'joshua senoron'})) # 'joshua senoron'

# element_from_set('edabit') # 'edabit' my test - works using print statement in function
# element_from_set({'edabit'}) # 'edabit' my test - works using print statement in function
# print(element_from_set('edabit')) # 'edabit' - works using return statement in function
