# About
Exercise: How to think cs - section 9.7, pg.103

# Exercise
As an exercise, test this function with some longer lists, and see if the number of values in each bucket tends to level off.

# Explanation
This exercise is based on a program that connects functions from the following sections:
 - 9.5, 
 - 9.6, and
 - 9.7.

Note: section 9.4 also forms part of the program. It explains how the random module works and shows you how to use a for loop to generate random numbers. The flow of execution is explained below.

# Flow of execution
- 1.Generate a list of random numbers # 9.5
- 2.Count the number of times a random value appears in the list of random numbers. The random value is from a range which is called a 'bucket.' # 9.6
- 3.Create many buckets to count the number of times a random value appears in different lists of random numbers. # 9.7

# Results

## Folders
- io: inputs and outputs.

## Differences
The differences below are the differences between the values of each bucket. The difference is based on a single pair, they don't overlap. Eg: 244-241 = 3 (pair one), 279-254 = 34 (pair two).

- 1k: 9, 11, 7, 8
- 2k: 3, 25, 19, 10
- 5k: 11, 68, 45, 27
- 10k: 8, 51, 36, 80
- 15k: 11, 29, 58, 73
- 20k: 112, 121, 122, 99
- 30k: 69, 107, 24, 37
- 50k: 98, 8, 40, 28
- 70k: 225, 6, 163, 133
- 100k: 98, 67, 8, 117

# Conclusion
The values of each bucket, in a set of eight, tend to stay in the same range or one that is relatively close. 
Eg: List length: 5k, Bucket values 1-8: [613, 624, 680, 612, 613, 658, 615, 588] - the first seven values are in the 600s and the last is 588 but relatively close to 600.

However, the deviation between each pair of buckets is varied. There is no discernable pattern and for the most part, the differences seem to be pretty wide between each pair. Subsequently, I would not say that longer lists yield bucket values that 'level off.'

Note: refer to io folder for inputs and outputs.