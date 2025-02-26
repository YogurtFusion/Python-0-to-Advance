'''for item in iteable:
'''
#use cases = lists, strings, dict and  ranges etc

'''
Key Functions:

range(start, stop, step): Generate sequences.

enumerate(iterable): Get index and value.

zip(iterables): Pair elements from multiple iterables.
'''

for i in range(1, 5):
    print(i)


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print (fruit)


# Print multiple times with out using range

fruits1 = ["apple", "oranges", "cheeries", "papaya"]

for i in fruits*6:
    print(fruits1)