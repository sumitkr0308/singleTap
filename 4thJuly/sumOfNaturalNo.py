#Sum of First N Natural Numbers
#Write a recursive function to find the sum of the first n natural numbers.

def sum(n):
    if n==1:
        return 1
    
    return n+sum(n-1)

n=int(input("Enter a number: "))
print(f"The sum of the first {n} natural numbers = {sum(n)}")