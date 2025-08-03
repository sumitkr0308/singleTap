#Fibonacci Sequence (Iterative)
#Write a function that prints the Fibonacci sequence up to n terms (without recursion).

def fibonacci(n):
    if n<=0:
        return []
    if n==1:
        return [0]
    first=0
    second=1
    ans=[first,second]
    i=3
    while i<=n:
        num=first+second
        ans.append(num)
        first=second
        second=num
        i+=1
    return ans    
num=int(input("Enter a number: "))
print(f"Fibonacci sequence upto {num} terms : {fibonacci(num)}")        
    
