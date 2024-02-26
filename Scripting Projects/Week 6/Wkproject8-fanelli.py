sourceFileName = input("Enter the name of the source text file: ")
destinationFileName = input("Enter the name of the destination text file: ")

sourceFile = open(sourceFileName, 'r')
fileContents = sourceFile.read()
sourceFile.close()

destinationFile = open(destinationFileName, 'w')
destinationFile.write(fileContents)
destinationFile.close()

print("Contents of '", sourceFileName, "' have been copied to '", destinationFileName, "' successfully.", sep="")

