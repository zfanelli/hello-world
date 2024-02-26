iterations = int(input("Enter the number of iterations for the π approximation: "))

result = 0
sign = 1


for i in range(1, iterations * 2, 2):
    term = sign * (1 / i)
    result += term
    sign *= -1

approx = result * 4

print("The approximation of π using " + str(iterations) + " iterations is: " + str(approx))
