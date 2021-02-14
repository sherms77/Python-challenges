# 071220: Decided to start again. Refer to countLetters3.py.

# How to think cs - Pg.79
# exercise 2
# i want to start counting from the index no. i specify

# find function takes a character and finds the index
def find(string, ch, start):    
    index = start
    while index < len(string):
        if string[index] == ch:
            return 'The index number of ' +ch+ ' is ' +str(index)+ '.'
        index = index + 1
    return 'The search started at index ' +str(start)+ '. \nSubsequently, the letter ' +ch+ ' has not been found.' 

# print(find('boxing', 'x', 0)) # should return 2
# print(find('boxing', 'x', 3)) # should return 'the character is not in the string.'

# countLetters function counts the number of times a letter appears in a string.
# you can set what letter it starts looking from by using the start paramater.
def countLetters(string, letter, start):
    print('The word is: ' +string)
    print('The letter to find is: ' +letter)
    # print('The letter the search started from is: ' +(string[start]) + ' which is index ') # insert index no. at the end.
    print(find(string, letter, start))

    # logic is to run through the find function first to determine if the character appears in the string based on the starting index.
    # if it is, run the for loop to count the number of times the character appears in the word.

    # need this to run if the find function returns an index no.
    # if find == True: 
   
    count = 0
    for char in string:
        if char == letter:
            count = count + 1
    print('\nRESULTS OF COUNT LETTERS FUNCTION')
    print('The number of times ' +letter+ ' appears in the word '+string+ ' is ' + str(count))

countLetters('boxing', 'x', 3) # should show that x does not appear in the word
# countLetters('boxing', 'x', 0) # should return a count of 1      
