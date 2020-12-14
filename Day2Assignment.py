#Assignment 1
#String Functions
var1="let's upgrade is Awesome"
var2="its Awesome"
print(var1.capitalize()) #Converts the first character to upper case
print(var1.endswith('s'))#Returns true if the string ends with the specified value
print(var1.isalpha())#Returns True if all characters in the string are in the alphabet
print(var1.replace("let's","Let"))#Returns a string where a specified value is replaced with a specified value
print(var1.split(" "))#Returns a string where a specified value is replaced with a specified value

#Assignment 2
#List Functions
fruits =["Apple","Banana","Orange"]
fruits.remove("Apple") #Removes the first item with the specified value
fruits

fruits =["Apple","Banana","Orange"]
fruits.append("Mango") #Adds an element at the end of the list
fruits

fruits.sort() #	Sorts the list
fruits

fruits.reverse()#Reverses the order of the list
fruits

fruits.pop(1) #Removes the element at the specified position
fruits

fruits.insert(0,"cherry") #Adds an element at the specified position
fruits

#Assignment 3
#Dictionary function
dit = {'name':'Sandeep', 'course':'python','mode':'online'}
dit.pop('name') #Removes the element with the specified key
dit

dit = {'name':'Sandeep', 'course':'python','mode':'online'}
dit.popitem() #Removes the last inserted key-value pair
dit

dit = {'name':'Sandeep', 'course':'python','mode':'online'}
dit.update({'inst':'Lets upgrade'}) #Updates the dictionary with the specified key-value pairs
dit

dit = {'name':'Sandeep', 'course':'python','mode':'online'}
dit.get("name") #Returns the value of the specified key
dit

dit = {'name':'Sandeep', 'course':'python','mode':'online'}
dit.clear() #Removes all the elements from the dictionary
dit


