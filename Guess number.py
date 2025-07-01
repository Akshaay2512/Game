# Guess the number

secret = 5
guess =0
attempt =0
max_Attempts=3

print("Welcome to the guessing Game :")
print("You have 5 attempts only ")

#initiate while loop to check for correct number and attempts:
while guess!=secret and attempt<=max_Attempts:
    print("You are on attempt " , attempt)
    guess=int(input("Enter yur guessed Number :"))
    if(guess > secret): # Range of numbers
        print("Try a lower number")
    else:
        print("Try a bigger number")
    attempt= attempt+1

if(guess==secret): # if correct number is entered
    print("Correct guess :" , guess ,"is the magical number")
else:
    print("You lost the game")


