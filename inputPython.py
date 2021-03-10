name_of_user = input("What is your first name?")
lenghtofusername = len(name_of_user)


lastnameofuser = input("What is your last name?")
lengthofuserlastname = len(lastnameofuser)

print("This is the length of the users first name ", lenghtofusername)
print(" This is the length of the users last name ", lengthofuserlastname)
print("The user name is %s %s " % (name_of_user, lastnameofuser))


#print("Hello %s %s, welcome to python" % name_of_user, lastnameofuser)
# if statements do something if a certain condition happens or doesnt happen
# underneath the if statement you need to indent your code to let the if statement know what code belongs to it.
# if tatements have if _your condition_ :
# else: code goes below it

if lenghtofusername > 0:
    nameofFriend = input("What is your friends name?")
    print("Your friends name is ", name_of_user)
else:
    print(" Please enter at least one letter...literally one letter")

    # While Loop
    # a condition will have to be true to keep your loop running
    # while(lenghtofusername is < 0):

    # indent every time
