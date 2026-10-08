n = int(input("Enter a number: "))

# def Digit_in_number(num):
#     count = 0
#     while(num>0):
#         rem = num%10
#         num = num//10
#         while(rem>0):
#             count += 1

# print(Digit_in_number(num))

def number_count(n):
    num = n 
    count = 0
    while(num > 0):
        dig = num % 10
        num //= 10
        count += 1
    print("Sum of digits is = ", count)

number_count(n)