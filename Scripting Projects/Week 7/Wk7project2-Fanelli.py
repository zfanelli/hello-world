fileName = input("Enter the filename: ")

with open(fileName, 'r') as file:
    lines = file.readlines()

lineCount = len(lines)

while True:
    print("Number of lines in the file:", lineCount)
    lineNumber = int(input("Enter a line number (0 to quit): "))
    
    if lineNumber == 0:
        break
    
    if 1 <= lineNumber <= lineCount:
        print("Line", lineNumber, ":", lines[lineNumber - 1])
    else:
        print("Invalid line number. Please enter a number between 1 and", lineCount)
