# Pg.66 How to think like a cs
# Code by Angie H, modified by Sherman B.

# Function prints each row
def createrow(n, row):    
    for i in range(1,n+1): # n+1 sets max in range
        print(i*row,'\t', end =' ') # added \t for symmetrical output
    print('\n')

def createtable(height, width):
    for i in range(1, height+1):
        createrow(i, i) # produces slanted output. Original line - createrow (width, i)

createtable(7,7)

# Flow of execution
# 1. Call createtable function.
# 2. Evaluate condition, is i in range 1 to height+1?
# 3. If yes, call createrow function.
# 4. Evaluate condition, is i in range 1 to n+1?
# 5. If yes, i multiplies row, tabs a space after result, prints on single line.
# 6. If i is less than n+1, execute each statement in the for loop and go back to step 4.
# 7. When the condition i in range 1 to n+1 is met, exit the for loop.
# 8. Execute the next statement. 
# 9. Go back to step 1, createtable function.
# 10. When the condition i is less than height+1 is met, exit the for loop.
