str = "qwertyuiopasdfghjklzxcvbnm1234567890,./;'[]-="

name = "shourya gupta"
firstName= name[0:7:1]
lastName= name[8:13:1]
funkyName= name[0:13:2]
reversedName= name[::-1]
print(firstName, lastName, funkyName, reversedName)

website = "http://google.com"
sliceURL = slice(7,-4)
print(website[sliceURL])

# format
pi = 3.142
largeNum = 1000000000000000000000000000000
emptyLine = '{} is a good man,always {action:10}'
print(emptyLine.format(name, action="helpfull"))

textArt = "pi is {pi:.2f}".format(pi=pi)
print("largenum = {:,}".format(largeNum))
print("largenum = {:b}".format(largeNum))