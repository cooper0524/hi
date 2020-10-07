import random

player = input("What's your name, Player? ")
print("Awesome! Let's play a game,", player, "!")


target = random.randint(1, 100)

while True:
    inputNum = input("Guess what Number am I!! ")
    checkInputNum = inputNum.isdigit()
    if checkInputNum:
        inputNum = int(inputNum)
        if inputNum == target:
            print("You Got Me!! Well Done!!!")
            break
        else:
            if target > inputNum:
                startNum = inputNum
                print("Naah! I'm bigger than you thought!!")
            else:
                endNum = inputNum
                print("Naah! I'm smaller than you thought!!")
    else:
        print("Make sure you're giving me a proper number,", player, "!")


    
   