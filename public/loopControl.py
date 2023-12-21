# break
# continue
# pass
run = True
while run:
    name = input("enter your name")
    if name != "":
        passcode = input("enter passcode or phone number")
    if passcode != "pass":
        print("done", end="")
        break