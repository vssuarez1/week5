#collection = single "variable" used to store multiple values
#list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#table = () ordered and unchangeable. Duplicates OK. FASTER 

# fruits = ["apple", "orange", "banana","coconut","kiwi","strawberry"] #lists
# fruits = {"apple","orange","banana","coconut"} #set
# print(fruits)
# #print(fruits[0]) #cannot do this with sets because unordered

# #SETs
# fruits.add("pineapple") 
# fruits.add("kiwi")
# fruits.remove("apple")
# print(fruits)
# fruits.pop () #pops off item at the end 
# fruits.clear #clears
# print(fruits)


#print(dir(fruits))
#print(help(fruits))
#print("pineapple" in fruits)
# # print(len(fruits))
# print(len(fruits)) 
# print("pinaeapple" in fruits) #checks for pineapple in list: boolean value if it is true or not 

# fruits[0] = "pineapple" #i can reassign values with this 
# print(fruits)


#LISTs
# fruits.append("pineapple") #add elements to the list
# #fruits.remove("apple") #removes elements 
# fruits.insert(0, "pineapple") #
# fruits.sort() #sorts the list
# fruits.reverse() #reverses the list
# fruits.clear() #clears the elements in the list 
# #print(fruits.index("coconut"))

# #for fruit in fruits:
# #print(fruit)

#TUPLEs
#print(dir(fruits))
#print(help(fruits))
#print("pineapple" in fruits)
# # print(len(fruits))
# print(len(fruits)) 

# print(fruits.index("apple")) 
# fruits = ("apple","orange","banana","coconut")
# print(fruits.count("coconut"))
# for fruit in fruits:
#     print(fruits)




# cars = ["bmw","maserati","audi","mercedes","ferrari"]
# print(f"these are the list of {cars}")
# print(f"the first car is {cars[0]}")


# #changing the value of the list
# cars[0] = "toyota"
# print(f"the first car is {cars[0]}")

# print(f"the last car is {cars[-1]}")
# cars[-1] = "lamborghini"
# print(f"the last car is {cars[-1]}")


# #adding a new value to the list
# cars.append("bugatti")
# print(cars)
# cars.remove("maserati")
# print(cars)


#looping thru the list
#otherwise called iterating thru the list 
#for car in cars: 
    #print(len(car))
    #print(car)
    #carRequest = input("add a car please")
    #cars.append(carRequest)
    #print(cars)
    #print(len(cars))
    #print(cars.upper())
    #print(cars)
   # if len(cars) > 10:
       # break

# friends = []
# addFriend = input("add a friend please: ")
# friends.append(addFriend)
# print(friends) 
# for friend in friends:
#     addFriend = input("add a friend please: ")
#     friends.append(addFriend)
#     print(friends)
#     if len(friends) > 6: 
#         break 
# friends.remove("idk")
# print(friends)


#DICTIONARIES
#dictionary = a collection of {key:value} pairs
#                     ordered and changeable. No duplicates 

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("USA"))
print(capitals.get("Japan"))
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")


capitals.update({"Germany":"Berlin"})
print(capitals)
capitals.update({"USA":"Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear

keys = capitals.keys()

print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(values)

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")


