# check if an element exists in a list or not
l=[]
n=int(input("Enter the size of list: "))

for i in range (0,n):
    element=input(f"Enter element {i+1}: ")
    l.append(element)

target=input("Enter the element to search: ")

if target in l:
    print(f"{target} is present in the list.")
else:
    print(f"{target} is present in the list.")    