#Even or Odd Checker
#Write a function that takes an integer and returns whether it is even or odd.

def checkEvenOdd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

num=int(input("Enter a number: "))
print(f"{num} is {checkEvenOdd(num)}")    