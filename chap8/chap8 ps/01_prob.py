def greatest (a, b, c):
    if ( a>b and a>c):
        return(a)
    elif ( b>a and b>c):
        return(b)
    elif (c>a and c>b):
        return c
    

chad = 1

bad = 234

sad = 233




#  print(greatest ( chad, bad, sad))

'''C:/Users/Anike/AppData/Local/Programs/Python/Python313/python.exe "c:/code per day/chap8/chap8 ps/01_prob.py"
  File "c:\code per day\chap8\chap8 ps\01_prob.py", line 19
    print(greatest ( chad, bad, sad))
IndentationError: unexpected indent
'''
print(greatest (a= chad, b= bad, c= sad))