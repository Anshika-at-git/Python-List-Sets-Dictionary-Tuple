n = int(input("Enter the number: "))

# def number(n):
#     rev = 0
#     while(n>0):
#         rem = n%10
#         rev = rev*10+rem
#         n = n//10
        
#     print(rev)

# number(n)

def digit_of_number(n):
    num = n
    while(num > 0):
        print(num % 10)
        num = num // 10
        
digit_of_number(n)