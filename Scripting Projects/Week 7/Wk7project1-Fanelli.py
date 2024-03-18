
def Mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def Median(numbers):
    if not numbers:
        return 0
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def Mode(numbers):
    if not numbers:
        return 0
    modeCount = {}
    for num in numbers:
        if num in modeCount:
            modeCount[num] += 1
        else:
            modeCount[num] = 1
    maxCount = max(modeCount.values())
    modes = [num for num, count in modeCount.items() if count == maxCount]
    return modes[0]

def Main():
    testList = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
    print("List:", testList)
    print("Mean:", Mean(testList))
    print("Median:", Median(testList))
    print("Mode:", Mode(testList))

if __name__ == "__main__":
    Main()
