print("bill classifier")

unit = int(input("Enter your unit: "))

if unit >= 0 and unit <= 100 :
    print("low consuption")

elif unit >= 101 and unit <= 250 :
    print("medium consuption")

elif unit >= 251 and unit <= 500 :
    print("high consuption")

elif unit >= 501 :
    print("very high consuption")


