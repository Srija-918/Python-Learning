#countingletter
count=0
word=input("Enter a word:")
for ch in word:
    if ch in "a":
        count=count+1
print("Number of a's =",count)