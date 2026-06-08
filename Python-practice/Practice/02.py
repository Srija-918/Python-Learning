#countingdigits
num=0
word=input("Enter any word:")
for ch in word:
    if ch.isdigit():
        num=num+1
print("Number of digits:",num)