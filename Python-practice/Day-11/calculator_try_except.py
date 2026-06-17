try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter another number:"))
    operator=input("Enter any basic arithmetic operator-+,-,*,/:")
    if operator=="+":
        print(num1+num2)
    elif  operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    else:
        print(num1/num2)
except ValueError:
    print("Invalid input..Enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

    