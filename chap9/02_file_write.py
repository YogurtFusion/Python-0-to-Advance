st = "please complete your doubts... "

f = open("my_file.txt", "w")

f.write(st)

f.close()


s = open("my_file.txt")
pet = s.read()
print(pet)
s.close()


st = "please complete your doubts... "

# Writing to the file
with open("my_file.txt", "w") as f:
    f.write(st)

# Reading from the file
with open("my_file.txt", "r") as s:
    pet = s.read()
    print(pet)




# sor = " second line of code \nthird line is yep i'm start working "
# w = open("file.txt", "w")
# w.write(sor)
# w.close()

sor = "did you got you answers of loops and your questions about your code \nsecond line of code \nthird line is yep i'm start working " 
w = open("file.txt", "w")
w.write(sor)
w.close()
