list = ["milk","rice","sugar","tomato "]

print(list)

#add
list.append("potato")
print(list)

#remove
list.remove("milk")
print(list)

#insert
list.insert(1,"oil")
print(list)

#sort
list.sort()
print(list)

rice_index = list.index("rice")
print(rice_index)

list[rice_index] = "basmati"

items = list.copy()

print("copied list",items)
print ("original",list)