#simple calculator
a,b = map(int, input("Enter two number :").split())
print("Enter the operation")
if input() == '+':
    print(a+b)
elif input() == '-':
    print(a-b)
elif input() == '*':
    print(a*b)
elif input() == '/':
    print(a/b)
else:
    print("Invalid operation")