
# ? high order func: accepts a function as an argument or returns a function


def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    Text = func("hello")
    print(Text)

def divisor(x):
    def divident(y):
        return y/x
    return divident

divide = divisor(2)
print(divide(10))