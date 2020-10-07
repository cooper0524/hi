checkDriveInput = False
while checkDriveInput is not True:
    drive = input("Have you drive before?")
    if drive != "yes" and drive != "no":
        print("Try just enter yes or no!")
    else:
        checkDriveInput = True
  
checkAgeInput = False
while checkAgeInput is not True:
    age = input("How old are you?")
    checkAgeInput = age.isdigit()
    if checkAgeInput is not True:
        print("Try just enter integer!")
    if checkAgeInput is True:
        break

if drive == "yes":
    if int(age) >= 18:
        print("Good citizen!")
    else:
        print("How dare you!")
else:
    if int(age) >= 18:
        print("Go get the license and get on the road!")
    else:
        print("Good boy!")

