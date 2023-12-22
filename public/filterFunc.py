
freinds = [
("a", 14),
("b", 21),
("c", 19),
("d", 15),
("e", 31)
]

age = lambda data:data[1]>= 18

newList = list(filter(age, freinds))
print(newList)