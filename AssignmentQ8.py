a = int(input("Enter an operand:"))
b = int(input("Enter another operand: "))
opr = input("Enter the operation need to be performed: ")

def calculator(a, b, opr):
    if( opr == "+"):
        result = a+b
    elif (opr == "-"):
        result = a-b
    elif (opr == "*"):
        result = a*b
    elif (opr == "/"):
        result = a/b
    else:
        print("Invalid operation.")

    return result

print(calculator(a, b, opr))