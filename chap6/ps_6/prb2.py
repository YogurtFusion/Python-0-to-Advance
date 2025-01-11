marks1 = (int(input("enter your marks1:")))
marks2= (int(input("enter your marks2:")))
marks3 = (int(input("enter your marks3:")))

#now total percentage of the student with respectives marks
totat_percentage = (100*(marks1+marks2+marks3))/300

print(totat_percentage)

if totat_percentage>=33 and marks1>=33 and marks2>=33 and marks3>=33:
    print("ok ok grade means average we can take it ")

else:
    print("haiyaaa!!!! you fucked up")