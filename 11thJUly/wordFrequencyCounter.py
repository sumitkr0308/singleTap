#Word Frequency Counter

def word_Frequency_Counter():
    text=input("Enter your text: ")
    cleaned_text=""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text+=char.lower()
        else:
            cleaned_text+=" "     # replace punctuation with space

    #split the words
    words=cleaned_text.split() 

    frequency={}

    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1

    for word,count in frequency.items():
        print(f"{word}: {count}") 

word_Frequency_Counter()             
                         
