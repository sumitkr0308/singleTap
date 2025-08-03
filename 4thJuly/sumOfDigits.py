#Sum of Digits
#Write a recursive function to return the sum of digits of a given number.

def sumOfDigits(n):
    if n==0:
        return 0
  
    return n%10 + sumOfDigits(n//10)

n=int(input("Enter a number: "))
print(f"The sum of digits of {n} = {sumOfDigits(n)} ")     