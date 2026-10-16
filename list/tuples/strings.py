name = "shikhar suthar"
print (name )
print(len(name))


text = "python"
print(text[0])
print(text[1])
print(text[-2])


#string slicing
#start
text = "python"
print(text[:3])
#middle
text = "python"
print(text[2:5])
#end
text = "python"
print(text[3:])

#complete string
text = "python"
print(text[:])


name = " shIkhAR sUtHar "
#strip function remove enpty spaces fron the both sides of the string
print(name.strip()) 
print(name.lstrip()) #remove empty spaces from left side of the string
print(name.rstrip()) #remove empty spaces from right side of the string

print(name.upper()) #convert string into upper case
print(name.lower()) #convert string into lower case

print(name.capitalize()) #convert first character of string into upper case and rest of the string into lower case

print(name.replace("suthar","parmar")) #replace the string with another string

text1 = "I like python"
text2 = "I like games"

new_text = text1.replace("python","java")
print(new_text)

print(text2.replace("like","love")) #replace the string with another string

#string cleaner and analyzer
string=input("Enter your idea:")

clean_string = string.strip().lower().replace(" ","_")
print(clean_string)

count = len(clean_string)#including spaces


count2=len(clean_string.replace(" ",""))#excluding spaces


