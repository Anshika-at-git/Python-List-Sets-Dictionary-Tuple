n = int(input("Enter a number: "))

def sum_of_digits(n):
    sum = 0
    while(n>0):
        rem = n%10
        sum = sum + rem
        n = n//10
    return sum


print(sum_of_digits(n))