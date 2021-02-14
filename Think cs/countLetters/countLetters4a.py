# Think cs: Pg.79 exercise
# based on hand written code - function without 3rd paramater
# task 3 from next steps_think cs doc

def count_letters4a(word, ch):
    count = 0
    for i in word:
        if i == ch:
            count = count + 1
    print(count)

count_letters4a('banana', 'a') # works - count is 3
count_letters4a('banana', 'n') # works count is 2
