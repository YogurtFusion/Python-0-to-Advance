with open ("log.txt", "r") as f:
    content = f.read()

if "python" in content :
    print(" yes python is present : ")

else:
    print ("nope python is not present")