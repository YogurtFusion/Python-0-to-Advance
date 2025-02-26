s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations

print(len(s)) # ask it about chat gpt why it is 2 not 3 because they both are diffrent types of data types