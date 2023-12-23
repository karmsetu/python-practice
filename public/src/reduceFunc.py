import functools
letters = [
'h',
'e',
'l',
'l',
'o',
]

factorial = [1,2,3,4,5,6]

word = functools.reduce(lambda x,y: x+y, letters)
result = functools.reduce(lambda x,y: x+y, factorial)
print(word, result)