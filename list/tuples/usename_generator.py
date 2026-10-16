name = input("Enter your name:")

clean_name = name.strip().lower().replace(" ", "")
year = int(input("Enter your year of birth:"))

if len(clean_name) == 0:
    print("name cannot be empty")
else:
    username = clean_name[0:4] + str(year)
    print("Your username is:", username)