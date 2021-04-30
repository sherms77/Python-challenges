n = int(input("Enter a value"))
print(n)

if (n > 1 and n < 100):
    if (n%2 == 0):
        if (n > 20):
            print("Not Weird")
        
        elif (n > 2 and n < 5):
            print("Not Weird")
        
        elif (n > 6 and n < 20):
            print("Weird")
    else:
        print("Weird")

else:
    print("Invalid input")

