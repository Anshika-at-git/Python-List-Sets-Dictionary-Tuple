# salary = int(input("Enter yoour salary: "))

# if (salary < 30000):
#     print("5% tax rate.")

# elif (salary >30000 and salary < 70000):
#     print("15% tax rate.")

# else:
#     print("25% tax rate.")

salary = int(input("Enter your salary: "))
# if(salary < 30000):
# 	taxRate = (salary * 5)/100
	
# elif(salary >= 30000 and salary < 70000):
# 	taxRate = (salary * 15)/100
# 	print("15%")
# else:
# 	taxRate = (salary * 25)/100

# print("Your Tax Rate is = ", taxRate)

def final_tax_rate(salary):
    if(salary < 30000):
        print("Tax Rate(5%) = ", (salary * 5)/100)
        
    elif(salary >= 30000 and salary < 70000):
        print("Tax Rate(15%) = ", (salary * 15)/100)
        
    else:
        print("Tax Rate(25%) = ", (salary * 25)/100)

final_tax_rate(salary)

