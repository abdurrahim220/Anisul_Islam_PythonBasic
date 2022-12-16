
'''
n1 = float(input("Enter number 1 : "))
n2 = float(input("Enter number 2 : "))
n3 = float(input("Enter number 3 : "))

if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)

else :
    print(n3)

m = (n1 if (n1>n2 and n1>n3) else
    (n2 if (n2>n1 and n2>n3) else n3))

print(m)

'''


ch = 'b'

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else :
    print("Consonant")
