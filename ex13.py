n = int(input("Enter the numbers you want to generate:"))

fibList = [0,1]

for i in range(2,n,1):
    fibList.append(fibList[i-1] + fibList[i-2]) 

print(fibList)