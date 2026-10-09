n = input("Enter a number (Type 'Quit' to exit): ")

def positive_negative(n):
    while(n != "Quit"):
        num = int(n)
        if(num > 0):
            print("Positive")
        else:
            print("Negative")

        n = input("Enter a number (Type 'Quit' to exit): ")

positive_negative(n)