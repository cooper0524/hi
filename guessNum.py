import random

player = input("What's your name, Player? ")
print("Awesome! Let's play a game,", player, "!")
print("You need to set up a range of numbers, and guess what Number am I!")

while True:
    startNum = input("Please give me a start number: ")
    checkStartNum = startNum.isdigit()
    endNum = input("Please give me a end number: ")
    checkEndNum = endNum.isdigit()
    if not checkStartNum or not checkEndNum:
        print("Make sure you're giving me an integer,", player, "!")
    else:
        startNum = int(startNum)
        endNum = int(endNum)
        if startNum >= endNum:
            print("Make sure you're giving me a proper range of numbers,", player, "!")
        else:
            target = random.randint(startNum, endNum)
            break
        
print("Great! All set up! Let's begin!!")

guessTimes = 0
while True:
    print("I'm between", startNum, "and", endNum, "!")
    inputNum = input("Guess what Number am I!! ")
    guessTimes += 1
    checkInputNum = inputNum.isdigit()
    if checkInputNum:
        inputNum = int(inputNum)
        if inputNum == target:
            print(target, "IT IS!! You Got Me!! Well Done!!! You have tried", guessTimes, "times in total!")
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
