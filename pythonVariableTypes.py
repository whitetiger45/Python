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
#---------------------------------------
dict = {}
print "Dict size: " + str(len(dict))

dict[1] = "one"
dict[2] = "two"

print "Dict size: " + str(len(dict))

dict = {3:"three", 4:"four"}

print "Dict size: " + str(len(dict))
c = 1

for x in dict:
    print "Key: " + str(x) + "\nValue: ", dict[x]

powerEx = 2**3
print "2^3: " + str(powerEx)

x = raw_input("\nEnter x: ")
y = raw_input("\nEnter y: ")
powerEx = int(x)**int(y)
print "\n" + str(x) + "^" + str(y) + ": " + str(powerEx)
# list(dict)
# for x in dict:
#     print "Key: " + str(x) + "\nValue: ", dict[x]
