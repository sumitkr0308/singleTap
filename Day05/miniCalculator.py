a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

operator=input("Choose the operation to be performed(+,-,*,/): ")

if(operator=='+'):
    print(f"Result= {a+b}")
elif(operator=='-'):
    print(f"Result= {a-b}")
elif(operator=='*'):
    print(f"Result= {a*b}") 
elif (operator=='/' and b!=0):
    print(f"Result= {a/b}") 
else:
    print("Error")           

