# print the factorial number using while loop 

n=int(input("Enter a number: "))

i=1
ans=1
while i<=n:
    ans*=i
    i+=1

print(f"The factorial of {n} is {ans}")    
