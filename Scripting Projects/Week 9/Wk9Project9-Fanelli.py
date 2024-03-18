def readNumbersFromFile(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print("Invalid number found in file:", line.strip())
    return numbers

def computeAverage(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

filename = input("Enter the filename: ")
try:
    numbers = readNumbersFromFile(filename)
    average = computeAverage(numbers)
    print("Average:", average)
except FileNotFoundError:
    print("File not found.")
