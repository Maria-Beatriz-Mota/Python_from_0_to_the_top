# with limited (3) attempts
Player = input("write your name: ")
print(f"Welcome {Player}!"
      f"\nGame rules: write down a number as you're trying to guess it."
      f"\n You're going to have 3 attempts. Good Luck!")
Guess_Number = 210
Total_Attempts = 3
Attempt = 1

while(Attempt <= Total_Attempts):
    print(f"attempt {Attempt} of {Total_Attempts}.\n")
    Guess_str = input("Write Your number guess: ")
    print(f" your Guess was {Guess_str}.\n")
    Guess = int(Guess_str)

    Right = Guess == Guess_Number
    Lower = Guess < Guess_Number
    Higher = Guess > Guess_Number

    if(Right):
        print("Congrats! You won the game!")
    else:
        if(Lower):
            print("You lost the game! :(\n the number you've picked is smaller than the correct one.")
        elif(Higher):
            print("You lost the game! :(\n the number you've picked is bigger than the correct one.")

    Attempt = Attempt + 1
