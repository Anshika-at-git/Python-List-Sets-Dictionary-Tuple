n = int(input("Guess a number: "))

num = 37

def guessing_game(n):
    if (n>num):
        print("Too high")
    elif (n<num):
        print("Too low")
    else:
        print("Correct!")

guessing_game(n)