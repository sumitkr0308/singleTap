#Power of a Number
#Write a recursive function to calculate a^b (a raised to the power b).
def power(n,m):
    if m==0:
        return 1
    elif m<0:
        return (1/n)*power(n,m+1)
    
    return n*power(n,m-1)

n=int(input("Enter a number: "))
m=int(input("Enter the power for a number: "))

print(f"{n} raised to the power {m} ({n}^{m}) = {power(n,m)}")