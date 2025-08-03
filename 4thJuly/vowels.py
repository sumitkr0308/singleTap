#Count Vowels in a String
#Write a function to count the number of vowels in a string.

def countVowel(s):
    count=0
    for i in range(0,len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
            count+=1

    return count
str=input("Enter a String: ")
print(f"Number of Vowels in {str} = {countVowel(str)}")        
