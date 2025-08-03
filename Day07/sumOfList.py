#find the sum of all element in a list
number=[]
n=int(input("Enter the size of list: "))

for i in range (0,n):
    element=int(input(f"Enter the number {i+1}: "))
    number.append(element)


sum=0
for i in range(0,n):
    sum+=(number[i])

print(f"Sum of all elemnets in a list is {sum}")        