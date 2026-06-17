dict={
    "name":"Srija",
    "age":19,
    "place":"hyd"
    }
try:
    key=input("Enter a key:")
    print(dict[key])
except KeyError:
    print("Enter a valid key")