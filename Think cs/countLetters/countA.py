# How to think cs - Pg.78
# example in 7.8 - count the number of times 'a' is in banana.
fruit = 'banana'
count = 0
for char in fruit:
    if char == 'a':
        count = count + 1
print(count) # returns 3
