marks= [45,56,76,87]
print (marks[2])

print("original marks ",marks)


#append
marks.append(33)
print("after adding ",marks)

#insert
marks.insert(3,49)
print("after inserting ",marks)

#remove
marks.remove(33)
print("after removing ",marks)

#sort
marks.sort()
print("after sorting ",marks)

#length
print ("total student ",len(marks))

#check exixting marks

print (76 in marks)
print (22 in marks)


# search marks

search = int(input("enter marks to search \n"))
print("marks status",search in marks)
# found = False


# for mark in marks:
#     if mark == search:
#        found = True

# if found:
#     print ("found")

# else:
#     print("not found")



