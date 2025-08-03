# sort a list in ascending and decending order

number=[]
n=int(input("Enter the size of list: "))

for i in range (0,n):
    element=int(input(f"Enter the number {i+1}: "))
    number.append(element)

#  Sort in Ascending Order
ascending=sorted(number)

print(f"List in ascending order: {ascending}")

# Sort in descending order
descending=sorted(number,reverse=True)
print(f"List in ascending order: {descending}")
