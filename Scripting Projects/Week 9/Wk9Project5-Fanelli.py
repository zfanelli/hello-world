def isSorted(lst):
    if len(lst) <= 1:
        return True
    
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    
    return True

# tests
print(isSorted([]))
print(isSorted([1]))
print(isSorted([1, 2, 3, 4, 5]))
print(isSorted([5, 4, 3, 2, 1]))
print(isSorted([1, 1, 1, 1, 1]))
print(isSorted([3, 2, 2, 1, 1]))

