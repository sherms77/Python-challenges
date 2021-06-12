# 110621: i have met the requirements of the exercise
# 110621: i have not implemented the code from 9.8 - single pass solution
# 110621: unsure if i should implement the code from 9.8?

# counts the values from each bucket
def inBucket(t, low, high):
    count = 0
    for num in t:
        if low < num < high:
            count = count + 1
    return count

# takes list and number of buckets as arguments and returns histogram with the given number of buckets
# l = list b = number of buckets
def histogram(l,b): 
    buckets = [0] * b # saves bucket counts
    bins = [0] * b # saves the bucket ranges
    width = 1.0 / b
    for i in range(b):
        low = i * width
        high = low + width
        bins[i] = (low, high) # stores bucket ranges in a list
        buckets[i] = inBucket(l, low, high)

    print('list entered is:', l)
    print('number of buckets created: ', b)

    print('\nBUCKET RANGES')
    count = 0
    for j in bins:
        count = count + 1
        print('bucket', count, 'range is:',j)

    print('\nCOUNTS\nthe number of times the values from each bucket is in the list is:')
    c = 0
    for k in buckets:
        c = c + 1
        print('from bucket:', c, 'is:',k)
    
# histogram([0.1,0.6,0.8],2) # bucket 1 = 1 bucket 2 = 2
histogram([0.1,0.6,0.7,0.8,0.9],2) # bucket 1 = 1 bucket 2 = 4

