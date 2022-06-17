def conditionalSum(values, condition):
    n = 0
    if condition =="even":
        for i in values:
            if (i%2)== 0:
                n = n + i
            else:
                continue
    elif condition == "odd":
        for i in values:
            if (i%2) > 0:
                n = n + i
            else:
                continue
    if n>0:
        return n
    else:
        return ("0")
    


print(conditionalSum([1, 2, 3, 4, 5], "even"))
print(conditionalSum([1, 2, 3, 4, 5], "odd"))
print(conditionalSum([13, 88, 12, 44, 99], "even"))
print(conditionalSum([], "odd"))