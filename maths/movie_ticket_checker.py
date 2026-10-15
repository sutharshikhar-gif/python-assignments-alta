print("welcome to the movie ticket booking system")
print("the price of a movie ticket is 200")

name = input("enter your name\n")
print("welcome", name)
movie_ticket_price = 200

age = int(input("enter your age\n"))
print("your age is ", age)

if age >= 60:
    print("you are eligible for senior citizen discount")
    discounted_price = movie_ticket_price * 0.8
    print("your discounted ticket price is ", discounted_price)

else:
    print("your ticket price is ", movie_ticket_price)

print("thank you for visiting our movie ticket booking system")
