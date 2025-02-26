marks = {
    "harry": 100,
    "shubam":34,
    "rohan":92
}

print(marks.get("harry2")) #output none
print(marks["harry2"]) #Bigbracket output none

d = {} #empty dict
s = set()#empty set 
# don't use s = {} as it will create empty dictt
print(type(s))

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations

print(len(s)) # ask it about chat gpt why it is 2 not 3 because they both are diffrent types of data types
