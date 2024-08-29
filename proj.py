import random
target = random.randint(1,100)

while True:
    userChoice = (input(" guess the no OR QUIT(Q) :"))
    if userChoice == "Q":
        print("u Quit")
        break
    userChoice =int(userChoice)

    if userChoice == target:
       print("Sucess :Correct guess ")
       break
    elif userChoice < target:
        print("your no was too small take another guess")
    else :
        print("your no was too large take another guess")

print("----GAME OVER----")