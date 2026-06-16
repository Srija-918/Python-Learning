file1=input("Enter the content to add into the file:")
file=open("user_note.txt","a")
file.write("\n"+file1)
file.close()