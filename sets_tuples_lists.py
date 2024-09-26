#collection = single "variable" used to store multiple values
#list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#table = () ordered and unchangeable. Duplicates OK. FASTER 

fruits = ["apple", "orange", "banana","coconut","kiwi","strawberry"]
print(fruits[0])



#print(dir(fruits))
# print(len(fruits))
print(len(fruits)) 
print("pinaeapple" in fruits) #checks for pineapple in list: boolean value if it is true or not 

fruits[0] = "pineapple" #i can reassign values with this 
print(fruits)

fruits.append("pineapple") #add elements to the list
fruits.remove("apple") #removes elements 
fruits.insert(0, "pineapple") #
fruits.sort() #sorts the list
fruits.reverse() #reverses the list
fruits.clear() #clears the elements in the list 


#for fruit in fruits:
#print(fruit)












