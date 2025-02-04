f = open("file.txt", "r")

print(f.read)

f.close

#The same can be written with "with statement" like below 
with open("file.txt") as f:
    print(f.read())

#You don't have to use f.close or explicitly close the file