import random

player = input("What's your name, Player? ")
print("Awesome! Let's play a game,", player, "!")


target = random.randint(1, 100)
guessTimes = 0
while True:
    inputNum = input("Guess what Number am I!! ")
    guessTimes += 1
    checkInputNum = inputNum.isdigit()
    if checkInputNum:
        inputNum = int(inputNum)
        if inputNum == target:
            print("You Got Me!! Well Done!!! You have tried", guessTimes, "times in total!")
            break
        else:
            if target > inputNum:
                startNum = inputNum
                print("Naah! I'm bigger than you thought!!You have tried", guessTimes, "times already!")
            else:
                endNum = inputNum
                print("Naah! I'm smaller than you thought!!You have tried", guessTimes, "times already!")
    else:
        print("Make sure you're giving me a proper number,", player, "!")


    
   