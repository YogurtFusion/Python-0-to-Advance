f = open("file.txt")

lines = f.readlines()
print(lines, type(lines))
f.close()
f = open("file.txt")
a = open("file.txt")
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line5 = f.readline()
print(line5 =="")

f.close ()


'''# gpt version
# Read all lines into a list
lines = f.readlines()
print(lines, type(lines))  # Prints the list of lines

# Reopen the file (to reset the pointer back to the start)
f.close()  # Close the first file handle

f = open("file.txt")  # Reopen the file

# Now we can read the lines one by one
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()  # This will read the third line now
print(line3, type(line3))

f.close()  # Finally, close the file 




'''