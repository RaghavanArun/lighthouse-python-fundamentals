def numberOfVowels(data):
    y = data.count('a') + data.count('e') + data.count('i') + data.count('o') + data.count('u')
    return (y)


print(numberOfVowels("orange"))
print(numberOfVowels("lighthouse labs"))
print(numberOfVowels("aeiou"))