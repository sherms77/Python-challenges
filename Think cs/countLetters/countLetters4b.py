# Think cs: Pg.79 exercise
# based on hand written code
# task 3 from next steps_think cs doc

def count_letters4b(word, ch, s): # s is starting index position, ch is specified character.
    count = 0 # initialises count
    e = len(word) # end of slice
    for i in word[s:e]: # loop condition. traverses and stores each character from string within slice in variable i.
        if i == ch: # compares i with ch. if its a match, counts it and stores in count variable on next line.
            count = count + 1 # counts each time ch is in word. adds it to variable each time ch is found.
    print(count) # prints count when loop has ended.

count_letters4b('banana', 'a', 2) # should be 2 - works
count_letters4b('banana', 'a', 0) # should be 3 - works
