san=input("Enter a sentence:")


clean_name=san.strip()

print(clean_name.upper())
print(clean_name.lower())

print(len(clean_name))
count=clean_name.replace(" ","")
print(len(count))


if len(count) < 5:
    print("name cannot be less than 5 characters")
else:
    print(count[0:4])
  