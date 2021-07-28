ABOUT
Exercise: How to think cs - pg.75.

The following example shows how to use concatenation and a for loop to generate an abecedarian series. "Abecedarian" refers to a series or list in which the elements appear in alphabetical order. For example, in Robert McCloskey's book "Make Wat for Ducklings", the names of the ducklings are Jack, Kack, Lack, Mack, Nack Ouack, Pack and Quack. This loop outputs the names in order:

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in  prefixes:
	print letter + suffix
	
Output:
Jack
Kack
Lack
Mack
Nack
Oack # should be Ouack
Pack
Qack # should be Quack

* "Ouack" and "Quack" are misspelled.

Exercise - As an exercise, modify the program to fix this error.

NOTES
- Above code is Python 2.
- Refer to abecedarian.py for solution.

STATUS
Finished - 28 July 2021