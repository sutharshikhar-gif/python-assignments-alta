# student=("rohit",20,"male")
# print(student)
# print (student[0])
# print (student[-1])

# int
# x=(1)
# print(type(x))

# tuple 
# x=(1,)
# print(type(x))

#normal indexing 

# student=("rohit",20,"male","CST")
# name = student[0]
# age = student[1]
# gender = student[2]
# course = student[3]

# print("Name:",name)
# print("Age:",age)
# print("Gender:",gender)
# print("Course:",course)

# #tuple unpacking
# student=("rohit",20,"male","CST")
# teacher=("Chaman",25,"male","IT")
# name,age,gender,course = student
# name,identity,gender,classs = teacher
# print("Name:",name)
# print("Age:",age)
# print("Gender:",gender)
# print("Course:",course)
# print("Teacher Name:",name)
# print("Teacher Age:",identity)
# print("Teacher Gender:",gender)
# print("Teacher Course:",classs)

# calculate percentage of student
student= ("rohit",100,90,70,60 )
name,maths,science,social,english = student
total = maths+science+social+english
percentage = (total/400)*100
print("Name:",name)
print("Total Marks:",total)
print("Percentage:",percentage)


a=(1,2,3,4,5)
b=(6,7,8,9,10)
c=a+b
print(c)