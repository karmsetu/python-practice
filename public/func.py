def hello(name=""):
    print("hello",name, "!", end=" ")

def givePow(num, pow=2):
    return int(num) ** pow
hello()
print(givePow(6,8))

# keyword arg
print(givePow(pow=30, num=69))

# args parameter # will wrap args in a tuple
def sum(*args):
    sum = 0
    for i in args:
        sum += int(i)
    return sum

print(sum(1,2,3,4,5,6,7,8,9,10))

# kwargs # will pack args in dictionary
def helloBoi(**kwargs):
    for key, value in kwargs.items():
        print(value, end=" ")

helloBoi(a="hello",b="mr",c="boi")