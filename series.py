#print  sum of 1 to n number


n = int(input("Enter the last number : "))

sum = 0

for x in range(2,n+1,2):
        sum += x
print(sum)


