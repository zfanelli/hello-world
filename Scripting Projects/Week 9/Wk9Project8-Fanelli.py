# updated version
def printall(seq):
    if seq:
        print("Argument:", seq)
        print("Current element:", seq[0])
        printall(seq[1:])

# test for the code
test_sequence = [1, 2, 3, 4, 5]
print("Testing with sequence:", test_sequence)
printall(test_sequence)
