file=open("user_note.txt","r")
count=0
content=file.read()
for i in content:
    count=count+1
print("No.of characters:",count)
file.close()