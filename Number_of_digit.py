numofLetter = 0
num0fWords = 0
num0fDigit = 0
numofSpecialChar = 0

text = input("Enter a text of numbers: ")

for x in text :
    x = x.lower()
    if (x >= 'a' and x <= 'z') :
        numofLetter += 1
    elif (x >= '0' and x<= '9') :
        num0fDigit += 1
    elif (x == ' ') :
        num0fWords += 1
    else:
        numofSpecialChar +=1

print(numofLetter)
print(num0fDigit)
print(num0fWords)
print(numofSpecialChar)