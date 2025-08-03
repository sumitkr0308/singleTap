#Reverse a String
#Write a recursive function to reverse a string.

def reverse(s):
    if len(s)<=1:
        return s
   
    return reverse(s[1:])+s[0]

str=input("Enter a String: ")

print(f"String after Reversed: {reverse(str)}")
