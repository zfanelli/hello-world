import random
import math

lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))

minGuesses = math.ceil(math.log2(upper - lower + 1))
print("Think of a number between", lower, "and", upper)
print("Try to mislead the computer")

count = 0
while True:
    guess = random.randint(lower, upper)
    count += 1
    print("Computer guesses:", guess)
    response = input("Is the guess too large (L), too small (S), or correct (C)? ").upper()

    if response == "C":
        print("Computer guessed it in", count, "guesses!")
        break
    elif response == "L":
        if guess == lower:
            print("You're cheating! The guess cannot be lower than the lower number.")
            continue
        upper = guess - 1
    elif response == "S":
        if guess == upper:
            print("You're cheating! The guess cannot be higher than the upper number.")
            continue
        lower = guess + 1
    else:
        print("Invalid response! Please enter L, S, or C.")

print("Minimum number of guesses required:", minGuesses)
