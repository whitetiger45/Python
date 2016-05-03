#!/usr/bin/python

x = raw_input("\nEnter x: ")
y = raw_input("\nEnter y: ")
op = raw_input("\nEnter an operand: ")

if op == "+" : 
    calc = int(x) + int(y)
elif op == "-":
    calc = int(x) - int(y)
elif op == "*" : 
    calc = int(x) * int(y)
elif op == "/":
    calc = int(x) / int(y)
elif op == "**":
    calc = int(x) ** int(y)

print "\n" + str(x) + str(op) + str(y) + ": " + str(calc) + "\n"