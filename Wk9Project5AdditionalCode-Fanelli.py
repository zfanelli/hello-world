def isSorted(lst, cmp_func=None):
    if len(lst) <= 1:
        return True
    
    if cmp_func is None:
        cmp_func = lambda x, y: x <= y  # Default comparison function for non-decreasing order
    
    for i in range(len(lst) - 1):
        if not cmp_func(lst[i], lst[i + 1]):
            return False
    
    return True

# Custom comparison function for non-increasing order (reverse sorted)
def reverse_cmp(x, y):
    return x >= y

# Tests with custom comparison function
print(isSorted([]))  # True
print(isSorted([1]))  # True
print(isSorted([1, 2, 3, 4, 5]))  # True
print(isSorted([5, 4, 3, 2, 1]))  # False
print(isSorted([1, 1, 1, 1, 1]))  # True
print(isSorted([3, 2, 2, 1, 1]))  # False
