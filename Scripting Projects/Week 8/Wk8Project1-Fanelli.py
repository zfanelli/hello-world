def newton(num):
    guess = num / 2.0
    while True:
        new_guess = (guess + num / guess) / 2.0
        if abs(new_guess - guess) < 0.0001:
            return new_guess
        guess = new_guess

print("Square Root Approximation using Newton's Method")
print("Enter a number to compute its square root or press Enter to exit.")
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        print("Exiting...")
        break
    try:
        num = float(user_input)
        if num < 0:
            print("Please enter a non-negative number.")
        else:
            result = newton(num)
            print(f"Square root of {num} is approximately: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
