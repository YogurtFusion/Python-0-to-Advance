word = "Donkey"

with open("file.txt", "r") as f: #Is this line is neccessary
    content = f.read()

contentNew = content.replace("word", "######")

with open("file.txt", "w") as f:
    f.write(contentNew)


