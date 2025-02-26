# Break: Exit the loop immediately
#continue: Skip the rest of the current iteraion
# pass: do nothing (just uses for skips the incomplete loops)
for num in range(10):
    if num == 3:
        continue
    if num == 7:
         break
    
    print(num)