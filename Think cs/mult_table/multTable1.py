# Pg.66 How to think like a cs

#Code by Angie H
#Function prints each row
def createrow(n, row):    
    for i in range(1,n+1):
        print(i*row, end ='  ')
    print('\n')

def createtable(height, width):    
    for i in range(1, height+1):
        createrow(width, i)
