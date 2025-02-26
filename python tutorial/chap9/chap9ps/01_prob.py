with open("poem.txt") as r:
    content = (r.read())
    print(content)
    if("twinkle" in content):
        print("Yep it is present in it ")
    else:
        print("nope it is not present")


# code by harry

f = open("poem.txt")
content1 = f.read()
if("twinkle" in content1):
    print("yes it is present in poem")
else:
    print("no, it's not present in the poem")