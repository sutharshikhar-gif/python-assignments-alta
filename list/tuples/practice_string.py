name=input("Enter your name:")


clean_name=name.strip().lower().replace(" ","_")
print(clean_name)

if len(clean_name) == 0:
    print("name cannot be empty")
else:
    print(clean_name[0])
    print(clean_name[-1])