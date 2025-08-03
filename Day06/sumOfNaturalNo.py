#2.sum of first n natural number using while loop

n=int(input("Enter a number: "))

sum=0
i=0
while i<=n:
    sum+=i
    i+=1

print(f"Sum of fisrt {n} natural number: {sum}")    