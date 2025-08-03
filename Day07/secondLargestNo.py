# find the second largest no. in a list
number=[]
n=int(input("Enter the size of list: "))

for i in range (0,n):
    num=int(input(f"Enter the number {i+1}: "))
    number.append(num)

first=second=float('-inf')   

for num in number:
    if num>first:
        second=first
        first=num
        
    elif num>second and num!=first:
        second=num


print(f"The second largest number in a list= {second}")