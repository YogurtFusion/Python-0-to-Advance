words = ["donkey", "gande", "bad"]

with open("second_file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("second_file.txt", "w") as f:
    f.write(content)