# How to think cs - Pg.79

# exercise 1
def countLetters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count = count + 1
    print(count)

countLetters('banana', 'a') 