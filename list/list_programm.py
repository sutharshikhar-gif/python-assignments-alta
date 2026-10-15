marks = [43,23,87,34]
print (marks[2])
print (marks)

#append 
marks.append(22)
print(marks)

#insert
marks.insert(2,33)
print (marks)

#remove
marks.remove(33)
print (marks)

#sort
marks.sort()
print (marks)

#length
print (len(marks))

#search
search = int(input("search:-"))
print(search in marks)

#find index
index = marks.index(87)

marks[index]= 80

print(marks)

#copy
numbers = marks.copy

print (numbers)
print(marks)
    


