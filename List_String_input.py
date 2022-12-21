
n = input("Enter a text of numbers : ")
# 10 20 30 40 .........
list = n.split() #10,20,30........

sum = 0

for num in list : 
    sum += int(num)

print(sum)

