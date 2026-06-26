import random

lower = 1
higher = 10
guesses = 0
number = random.randint(lower, higher)

while True:
    guess = int(input(f"Guess the Number between ({lower} - {higher}) : "))
    guesses+=1

    if guess < number :
        print("Your guess is too LOW!!")
    elif guess > number:
        print("Your guess is too HIGH")
    else:
        print(f"You Guessed the correct number : {number}")
        break
print(f"The total Guess you too is : {guesses}")