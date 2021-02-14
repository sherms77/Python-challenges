# How to think cs - Pg.79
# exercise 2 v2

# counts the number of times the letter appears in the string
# starts counting from the index in the start paramater

def countLetters(string, letter, start):
    i = start
    count = 0
    while i < len(string):
        if string[i] == letter:
            for char in string:
                if char == letter:
                    count = count + 1
            return letter+ ' appears in the word ' +string+ ' ' +str(count)+ ' times.'
        i +=1
    return 'The count started from index number ' +str(start)+ '\nSubsequently, the letter ' +letter+ ' does not appear in the word ' +string+ '.'

print(countLetters('boxing', 'x', 3)) # works - result is not in word
print(countLetters('boxing', 'x', 0)) # works - resutlt is 1


# same function but uses print instead of return
# can't get it to work using print statements
# it works for a start index that lets it traverse the entire string
# but does not work for the alternative
# if you don't have an alternative condition it works, whereby there is no output if start index is after the letter index

def countLetters2(string, letter, start):
    i = start
    count = 0
    while i < len(string):
        if string[i] == letter:
            for char in string:
                if char == letter:
                    count = count + 1
            print(letter+ ' appears in the word ' +string+ ' ' +str(count)+ ' times.')
        i +=1

    # print('Not in word')
    # break
    
    # if i != 0:
        # print('Not in word.')   
        
    # if string[i] != letter:
        # print('The count started from index number ' +str(start)+ '\nSubsequently, the letter ' +letter+ ' does not appear in the word ' +string+ '.')
        
countLetters2('boxing', 'x', 3) # result should be not in word
countLetters2('boxing', 'x', 0) # works - result should be 1
