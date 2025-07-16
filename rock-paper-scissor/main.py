import random

options=["rock" , "paper" , "scissors"]

userChoice=input("enter rock , paper or sciisors :")
botChoice =random.choice(options)

print(f"you choose : {userChoice} \nbot choose : {botChoice}")

if userChoice == botChoice:
    print("its a tie !")

elif (userChoice == "rock" and botChoice =="scissors") or (userChoice=="paper" and botChoice=="rock") or (userChoice=="scissors" and botChoice=="paper"):
    print("you won the game !")

else :
    print("you lost the game !")
