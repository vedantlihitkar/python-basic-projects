#snake water gun game
# g = 1
# w = -1
# s = 0

import random


compOption = random.choice([-1, 0, 1])

yourOptions ={"g" : 1 , "w" : -1 , "s" :0}
compOptionsAvailable ={1 : "gun", -1: "water", 0: "snake"}


you=input("enter your choice :")

actualUserValue=yourOptions[you]

print(f"your choice {compOptionsAvailable[actualUserValue]} and computer choice {compOptionsAvailable[compOption]}")

if compOption==-1 and actualUserValue==-1:
    print("match draw ")

elif compOption==-1 and actualUserValue==1:
    print("computer win ")

elif compOption==-1 and actualUserValue==0:
    print("you win ")

elif compOption==1 and actualUserValue==-1:
    print("you win ")

elif compOption==1 and actualUserValue==1:
    print("match draw ")

elif compOption==1 and actualUserValue==0:
    print("computer win ")

elif compOption==0 and actualUserValue==-1:
    print("computer win ")

elif compOption==0 and actualUserValue==1:
    print("you win ")
elif compOption==0 and actualUserValue==0:
    print("match draw ")

else:
    print("invalid input")


