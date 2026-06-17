list=["apple","banana","orange"]
try:
    index=int(input("Enter an index:"))
    print(list[index])
except IndexError:
    print("Index out of range...Enter the valid index")