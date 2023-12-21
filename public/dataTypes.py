
age = 18
temp = 48.5
isMale = True
n =7
# multiple assignment
firstName, lastName = "shourya", "gupta"
print((firstName, lastName))

# string methods
print(len(firstName)) #gives length
print(firstName.find('o')) #finds the char and returns index
print(firstName.capitalize()) #finds the char and returns index
print(firstName.upper()) #finds the char and returns index
print(firstName.lower()) #finds the char and returns index
print(firstName.isdigit()) #finds the char and returns index
print(firstName.isalpha()) #Alphabetical letters
print(firstName.count('h')) #finds the char and returns index
print(firstName.replace('o','a')) #finds the char and returns index
print(firstName*n) #repeats the str n times

#typecasting
floatToInt = int(temp)
print(floatToInt) #finds the char and returns index

# List
list1 = ["a", "b","c","d","e","f"]
list1[5] = "g"
print(list1.append("f"))
print(list1.remove("a"))
print(list1.pop())
print(list1.insert(0, "lol"))
print(list1.sort())
print(list1.clear())


# 2d lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# tuples # cante be changed

stdTpl = (1,2,3,4,5,6,7,8,9,0)
print(stdTpl.count(1))
print(stdTpl.index(4))
print(stdTpl.index(4))

# sets #unique char/elements
setB = {"fork", "spoon", "knife"}
setA = {"bowl", "plate", "cup"}
setB.add("napkin")
setB.remove("spoon")
setB.clear()
setB.update(setA)
print(setB)

# dictionary #key-value pairs
country = {
    "India":"delhi",
    "USA":"washington DC",
    "Germany":"berlin",
    "France":"paris",
    "Russia":"moscow"
}
country.update({"Nepal":"Kathmandu"})
country.update({"Nepal":"kathmandu"})
country.pop("USA")
country.clear()
# print(country['Nepal'])
print("data",country.get("delhi"))
print(country.keys())
print(country.values())
print(country.items())

# index operator []= gives access to a sequence
name = "bro code"

print(name[0:3])