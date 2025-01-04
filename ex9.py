import random

rNum = random.randint(1,10)

while(True):
    num = int(input("Guess the number! "))

    if(num > rNum):
        print("Too high!")

    elif(num < rNum):
        print("Too low")

    else :
        print("You are right")
        break