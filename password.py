password = "a123456"
leftTimes = 3

while leftTimes > 0:
    inputValue = input("Please enter password: ")
    leftTimes -= 1
    if inputValue == password:
        print("Login success!")
        break
    else:
        print("Invalide password! You have ", leftTimes, " times left!" )
        if leftTimes == 0:
            print("Account locked!")
