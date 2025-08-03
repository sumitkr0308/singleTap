#print the square of each element in  list
number=[]
n=int(input("Enter the size of list: "))

for i in range (0,n):
    element=int(input(f"Enter the number {i+1}: "))
    number.append(element)

for i in range(0,n):
    print(f"Square of {number[i]} = {number[i]**2}")
