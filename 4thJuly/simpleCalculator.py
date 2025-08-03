#Simple Calculator
#Create a function that performs add, subtract, multiply, divide based on user inputSum  of Two Numbers

def calculate(a,op,b):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b!=0:
            return a/b
        else:
           return "Error: Division by zero is not allowed!" 

    else:
        return "Error: Invalid Operator!"
a=float(input("Enter 1st number: ")) 
b=float(input("Enter 2nd number: ")) 
op=input("Select Operation to be performed (+,-,*,/): ") 
print(f"Answer = {calculate(a,op,b)}")


