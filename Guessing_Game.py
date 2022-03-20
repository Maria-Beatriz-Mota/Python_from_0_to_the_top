# with choose how many times to play till getting the right answer or till giving up and stop the game.
Player = input("write your name: ")
print("Welcome! Are you ready to play", Player, end="?\n")
Choice = int(input("choose 1 if yes or 2 if not: "))
''' coments to do '''
while True:

    Answer = 210
    if Choice == 1:
        Number_str = (input(f"Game rules: write down a number as you're trying to guess it.\nChoose your number: "))
        Number = int(Number_str)
        Right = Number == Answer
        Op1 = Number > Answer
        Op2 = Number < Answer
        if Right:
            print("You Won the game! Congrates my fellow :)\n")
            break
        else:
            print("You lost the game! :(")

            if Op1:
                print("tips: The number you've picked is bigger than the correct answer.")

            elif Op2:
                print("tips: The number you've picked is smaller than the correct answer.")

            Op = int(input("selecte 1 to exit the game or 2 to try again."))
            if Op == 1:
                print("GOODBYE!\n")
                break
            if Op == 2:
                print("____________________________")

    elif Choice == 2:
        print("GET OUT!\n")
        break

    else:
        print("you have chosen any number option! restart the game.\n")
        break
