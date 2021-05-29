# About
How to think cs - section 9.7, pg.103

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

# Exercise
As an exercise, test this function with some longer lists, and see if the number of values in each bucket tends to level off.

# Results
note: reassess this. 2k list size shows better levelling off.

The number of values in each bucket start to level off with a list size of 50k. They start to stay with in the same range and incrementally go up and down but within a pretty tight range. Ie: counts start in the 6300 range and then goes into the the 6200 range and incrementally moves up and down within the 6200s.

# Folders
- io: inputs and outputs.
