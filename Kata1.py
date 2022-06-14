def sumLargestNumbers(x):
    y= max(x)
    x.remove(y)
    z= max(x)
    return (y+z)


print(sumLargestNumbers([1, 10]))
print(sumLargestNumbers([1, 2, 3]))
print(sumLargestNumbers([10, 4, 34, 6, 92, 2]))
