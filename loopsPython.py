nameofuser = input("what is your name")
lenghtofusername = len(nameofuser)

while (lenghtofusername < 0):
    nameofuser = input("what is your name")
    lenghtofusername = len(nameofuser)
print("The username is %s" % (nameofuser))
