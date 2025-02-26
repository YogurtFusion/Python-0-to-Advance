n = int(input("Enter your number: "))


for i in range(2, n):
    if(n%i) == 0:
        print("number is not prime")
        break
else:
    print("number is prime")


#Question 

'''C:/Users/Anike/AppData/Local/Programs/Python/Python313/python.exe "c:/code per day/chap7/chap7 ps/04_prob.py"
Enter your number: 4436789344236789Traceback (most recent call last):
  File "c:\code per day\chap7\chap7 ps\04_prob.py", line 1, in <module>
    n = int(input("Enter your number: "))
            ~~~~~^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt'''


