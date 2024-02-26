side1 = float(input("Enter the length of the first side: "))

side2 = float(input("Enter the length of the second side: "))

side3 = float(input("Enter the length of the third side: "))

if side1 > side2 and side1 > side3:
    hypotenuse = side1
    sumSides = side2 ** 2 + side3 ** 2
elif side2 > side1 and side2 > side3:
    hypotenuse = side2
    sumSides = side1 ** 2 + side3 ** 2
else:
    hypotenuse = side3
    sumSides = side1 ** 2 + side2 ** 2

if hypotenuse ** 2 == sumSides:
    print("It's a right triangle.")
else:
    print("It's not a right triangle.")
