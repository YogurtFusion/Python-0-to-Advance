n = (int(input("Enter your no. for table: ")))

table =  [n*i for i in  range (1, 11)]
with open ("table.txt", "a")as f:
    f.write(f"Table of {n}: {(table)}\n")


#Harry's code


n = (int(input("Enter your no. for table: ")))

table =  [n*i for i in  range (1, 11)]
with open ("table.txt", "a")as f:
    f.write(f"Table of {n}: {str(table)}\n")
