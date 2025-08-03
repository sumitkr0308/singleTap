# remove duplicates from a list

l=[1,1,23,45,6,"sumit",456]
unique=[]

for i in range (0,len(l)):
    if l[i] not in unique:
        unique.append(l[i])

print(f"Original list: {l}")   
print(f"The list after removing duplicates: {unique}")        