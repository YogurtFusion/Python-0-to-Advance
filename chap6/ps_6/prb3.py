p1 = "make a lot of money "
p2 = "click on my bio"
p3= "buy now"
p4 = "subscribe to my channekl"

message = input("enter your message:")

if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("spam message")

else:
    print("grnuine message")


