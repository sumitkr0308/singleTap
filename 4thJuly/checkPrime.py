#Check Prime Number
#Write a function to check if a number is prime.

def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False

    return True

num=int(input("Enter a number: "))

if(prime(num)):
    print(f"{num} is a Prime number.")
else:
     print(f"{num} is not a Prime number.")   
        
