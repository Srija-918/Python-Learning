try:
    marks=int(input("Enter your marks:"))
    print("you scored", marks, "marks")
except ValueError:
    print("Invalid value")