st = "hey mai this hu \nmujhe bhott maje aa rhe hai \nmujhe kasthuri mehthi bhott achi lag rhi hai"

with open ("this.txt", "w") as f:
    f.write(st)

with open("this.txt") as f:
    content =  f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)