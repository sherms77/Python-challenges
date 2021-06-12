# Think cs 9.5-9.7

import random

# 9.5 - random numbers list
def randomList(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s

# 9.6 - count random value
def inBucket(t, low, high):
    count = 0
    for num in t:
        if low < num < high:
            count = count + 1
    return count

# 9.7 - many buckets
x = int(input('Enter the number of buckets you want to create: ')) # number of buckets to create
numBuckets = x
buckets = [0] * numBuckets
bucketWidth = 1.0 / numBuckets
y = int(input('Enter a size for the random numbers list: ')) # size of random numbers list
for i in range(numBuckets):
    low = i * bucketWidth
    high = low + bucketWidth
    buckets[i] = inBucket(randomList(y), low, high) # buckets[i] = inBucket(t, low, high) # randomList - list of random vals is generated each time through the loop? shouldn't count vals from the same list?
    
print(buckets)

