with open("old.txt") as f:
    content = f.read()

with open("renamed_by_ python.txt", "w") as d:
    d.write(content)