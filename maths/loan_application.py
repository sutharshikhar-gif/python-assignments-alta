# loan application

name = input("enter your name\n")
print("welcome", name)

salary = float(input("enter your salary\n"))
print("your salary is ", salary)

phone = int(input("enter your phone number\n"))
print("your phone number is ", phone)

# arithmetic concepts

existing_emi = float(input("enter your existing monthly emi\n"))

available_income = salary - existing_emi
min_salary = 30000
min_available_income = 20000

print("your available income is ", available_income)


# print(10>5) # True
# print(10<5) # False
# print(10==5) # False
# print(10!=5) # True

# salary = 200000 assigned to salary variable
# salary == 200000 compares the value of salary with 200000

if salary >= min_salary :
    if available_income >= min_available_income:
        print("congratulations! you are eligible for loan")
    else:
        print("salary is sufficient but your available income is not sufficient for loan")
else:
    print("you are not eligible for loan")
    print ("your salary is less than minimum salary required for loan")

print("thank you for visiting our loan eligibility portal")











