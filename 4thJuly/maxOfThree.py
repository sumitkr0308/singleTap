#Find Maximum of Three Numbers
#Write a function that takes three numbers and returns the largest one.

def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
a=int(input("Enter 1st number: "))    
b=int(input("Enter 2nd number: ")) 
c=int(input("Enter 3rd number: ")) 
print(f"The Largest number is {largest(a,b,c)}.")