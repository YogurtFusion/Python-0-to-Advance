try:
    a = int(input("Heyy, Enter your number: "))
    print(a)

except ValueError as v:
    print("Heyyyyy")
    print(v)

except Exception as e:
    print(e)

print("Thank you")