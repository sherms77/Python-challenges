import random

def randomList(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s

def inBucket(t, low, high):
    count = 0
    for num in t:
        if low < num < high:
            count = count + 1
    return count

# print(inBucket([4.0,5.0,8.0], 3.0,9.0))
# print(inBucket([4,5,8], 3.0,9.0))
# print(inBucket([4,5,8], 3,9))
# print(inBucket([4,5,8], 1,5))

# creates buckets
def buckets(k,l): # k = num buckets l = list
    num = k
    bins = [0] * num
    width = 1.0 / num
    for b in range(num):
        low = b * width
        high = low + width
        bins[b] = (low, high)
    print(bins)

    count = 0
    for num in l:
        if low < num < high:
            count = count + 1
    print(count)

buckets(2)

'''
def histogram(l,b): # l = size of list b = number of buckets
    numBuckets = b
    buckets = [0] * numBuckets
    bucketWidth = 1.0 / numBuckets
    for i in range(numBuckets):
        low = i * bucketWidth
        high = low + bucketWidth
        # buckets[i] = inBucket(randomList(l), low, high)
        buckets[i] = inBucket(l, low, high)

    print(buckets)

# histogram([3,4,5,6], 8) # produces eight zeroes?
l = randomList(5)
j = [3,4,5,6]
# histogram(l, 8) # produces [1, 1, 1, 1, 1, 0, 0, 0]
# histogram(j, 8) # also produces eight zeroes?
    
# histogram does what the exercise in 9.8 asks - takes a list and a number of buckets as arguments and returns a histogram with the given number of buckets.
# however, it does not perform a 'single pass' or stores the buckets in a list to give each bucket an index as discussed in 9.8.
'''
