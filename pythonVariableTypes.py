#!/usr/bin/python

x = 100;
y = 101.0;
z = 103.09;

print x * 2
print y + z
print "Y: " + str(z)

statement = "Hello world"
print statement[:]
print statement[0:4] + " There"
print "In this crazy " + statement[6:]

listOfThings = [1, statement, x, y, "This is the end!"]
print listOfThings[:]
print listOfThings[1:3]
print listOfThings[3] + y

tuple = ('today', ' is',' a good day')
print tuple
print str(str(tuple[0:2]) + str(tuple[len(tuple)-1]))
s = "\n"
for x in tuple:
    s += x
    print str(x)

s += "\n"
print s