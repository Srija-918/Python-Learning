name=input("Enter a name: ")
count=0
for ch in name:
    if ch in "aeiou":
        count=count+1
print("number of vowels: ",count)