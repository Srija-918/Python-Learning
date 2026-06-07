count=0
word=input("Enter a word: ")
for ch in word:
    if ch in "aeiou":
        count=count+1
print("number of vowels:",count)