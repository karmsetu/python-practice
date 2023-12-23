squares =[]
marks = [12,30,45,63,84,0,14,6,85]
for i in range(1,11):
    squares.append(i*i)
print(squares)
squares1 = [i*i for i in range(1,11)]
print(squares1)

passed = [i for i in marks if i>=50]
print(passed)