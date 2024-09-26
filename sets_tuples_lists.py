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
#fruits.remove("apple") #removes elements 
fruits.insert(0, "pineapple") #
fruits.sort() #sorts the list
fruits.reverse() #reverses the list
fruits.clear() #clears the elements in the list 
#print(fruits.index("coconut"))

#for fruit in fruits:
#print(fruit)



cars = ["bmw","maserati","audi","mercedes","ferrari"]
print(f"these are the list of {cars}")
print(f"the first car is {cars[0]}")


#changing the value of the list
cars[0] = "toyota"
print(f"the first car is {cars[0]}")

print(f"the last car is {cars[-1]}")
cars[-1] = "lamborghini"
print(f"the last car is {cars[-1]}")


#adding a new value to the list
cars.append("bugatti")
print(cars)
cars.remove("maserati")
print(cars)


#looping thru the list
#otherwise called iterating thru the list 
for car in cars: 
    #print(len(car))
    #print(car)
    carRequest = input("add a car please")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    print(cars.upper())
    print(cars)
    if len(cars) > 10:
        break









