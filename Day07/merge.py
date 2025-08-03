l1=[]
n1=int(input("Enter the size of List 1: "))

for i in range (0,n1):
    elem=input(f"Enter the element {i+1}: ")
    l1.append(elem)

l2=[]
n2=int(input("Enter the size of List 2: "))

for i in range (0,n2):
    elem=input(f"Enter the element {i+1}: ")
    l2.append(elem)

print(f"List 1: {l1}")
print(f"List 2: {l2}")

# merge list
# merge=l1+l2  //method 1
l1.extend(l2)

print(f"Merged List: {l1}")
