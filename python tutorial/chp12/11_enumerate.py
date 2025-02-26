l = [3, 342, 45 , 535]

index = 0
for item in l:
    print(f"The item no. at {index} is {item}")
    index += 1

    #This can be simplified using enumerate function


for index, item in enumerate(l):
    print(f"the item at index {index} is {item}")