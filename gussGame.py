from random import randint

for x in range(1, 6):
    gussNumber = int(input("Enter your guess between 1 to 5 : "))
    randomNumber = randint(1, 5)

    if gussNumber == randomNumber:
        print("You Have Won !!")
    else:
        print("You have lost!!")
        print("The random number was: ", randomNumber)
