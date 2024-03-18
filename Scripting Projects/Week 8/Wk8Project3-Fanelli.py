def newton(num, initialGuess=None):
    if initialGuess is None:
        initialGuess = num / 2.0
    
    newGuess = (initialGuess + num / initialGuess) / 2.0
    if abs(newGuess - initialGuess) < 0.0001:
        return newGuess
    else:
        return newton(num, newGuess)

print("Square Root Approximation using Newton's Method")
print("Enter a number to compute its square root or press Enter to exit.")
while True:
    userInput = input("Enter a number: ")
    if userInput == "":
        print("Exiting...")
        break
    try:
        num = float(userInput)
        if num < 0:
            print("Please enter a non-negative number.")
        else:
            result = newton(num)
            print(f"Square root of {num} is approximately: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
