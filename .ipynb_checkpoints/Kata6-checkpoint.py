def urlEncode(text):
    y = text.strip()
    z = y.split(" ")
    k = ""
    for i in z:
        k = k + i + "20%"
    
    return (k.)


print(urlEncode("Lighthouse Labs"))
print(urlEncode(" Lighthouse Labs  "))
print(urlEncode("blue is greener than purple for sure"))