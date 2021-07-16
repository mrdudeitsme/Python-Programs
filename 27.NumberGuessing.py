winning_number = 25
Guess_number = int(input("Guess a number between 1 to 100:"))

if Guess_number == winning_number:
    print("You Win")
else:
    if Guess_number < winning_number:
        print ("To high")
    else:
        print("Too high")
