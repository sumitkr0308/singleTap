a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

if a<b and a<c:
    print(f"The smallest number: {a}")
elif b<a and b<c:
    print(f"The smallest number: {b}") 
else:
     print(f"The smallest number: {c}")       