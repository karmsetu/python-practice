
# ? applies a func to each iterable

list1 = [
    ("shirt", 20),
    ("pants", 25),
    ("jeans", 30)
]

to_euro = lambda data: (data[0], data[1]*.82)

store_euro = list(map(to_euro, list1))

print(store_euro)