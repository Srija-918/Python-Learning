file=open("user_note.txt","r")
count=0
for line in file:
    count=count+1
print("Number of lines:",count)
file.close()