print("age classifier")

age = int(input("Enter your age : "))

if 0<=age<=1 :
    print("you are an infant")

elif 1< age<=12 :
    print ("you are a child") 

elif 13 < age <= 17 :
    print (" you are teenager")

elif 18 < age <= 40 :
    print (" you are adult")

elif 40 < age <= 60 :
    print (" you are middle aged adult")

elif 60 < age <= 100 :
    print (" you are old")

else :
    print ("are jao na chacha kitna jiyoge")
