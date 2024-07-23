
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if b == 0:
        return "Error! Division with 0 is not possible"
    return a/b


print("The available operations\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n")
print("\n")

choice = input("Enter the operation (1/2/3/4): ")

if choice in ['1','2','3','4']:
    if choice == '1':
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print(add(num1,num2))
    elif choice == '2':
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print(subtract(num1,num2))
    elif choice == '3':
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print(multiply(num1,num2))
    elif choice == '4':
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print(division(num1,num2))
else :
    print("Invalid Entry")    
    


