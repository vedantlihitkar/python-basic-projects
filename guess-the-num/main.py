# import random

# compGuess=random.randint(1 ,100)
# # userChoice =int(input(f"guess the number between 1  to 100 :"))
# guesses =0
# userChoice = -1
# while (userChoice != compGuess):
#     userChoice =int(input(f"guess the number between 1 to 100 :"))
#     if userChoice < compGuess:
#         print("higher number please ")
#     elif (userChoice > compGuess):
#        print("lower number please")
#     guesses +=1
    
# print(f"you have entered correct number in{guesses} attempts")




import random


while True :
    print("new game has been started ")

    computerChoice=random.randint(1,100)
    print(computerChoice)
    userChoice =-1
    guess =0

    while (userChoice != computerChoice ):
            guess +=1
            userChoice=int(input("enter the number between 1 to 100 :"))
            if userChoice > computerChoice:
               print("guess lower number")
            elif userChoice<computerChoice:
              print("guess greater number")

            else:
               print(f"you guessed the right number in {guess} attempts")


            if guess == 5 :
                print(" you failed")
                break



    playAgain = input("enter yes / no to play the game ").lower()

    if playAgain != "yes":
        print("thank you for playing")
        break

