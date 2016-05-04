#!/usr/bin/python
calculate = 1
while calculate :
    x = raw_input("\nEnter x: ")
    y = raw_input("\nEnter y: ")

    ops = ['1) +', '2) -', '3) *', '4) /', '5) **', '6) //']
    print "\nOptions:\n_________\n"
    for c in ops:
        print str(c)

    op = raw_input("\nEnter an operand: ")
#-------------------------------------------------------------------------
    if op == "+" : 
        calc = int(x) + int(y)
    elif op == "-":
        calc = int(x) - int(y)
    elif op == "*" : 
        calc = int(x) * int(y)
    elif op == "/":
        if int(y) == 0:
            print "Cannot divide by 0\n"
        else:
            calc = int(x) / int(y)
    elif op == "**":
        calc = int(x) ** int(y)
    elif op == "//":
        if int(y) == 0:
            print "Cannot divide by 0\n"
        else:
            calc = int(x) // int(y)
#-------------------------------------------------------------------------
    if int(y) != 0:
        print "\n" + str(x) + str(op) + str(y) + ": " + str(calc) + "\n"
    
    calculate = raw_input("\nYou want to continue (yes/no): ")
    if str(calculate) == "yes":
        calculate = int(1)
    elif str(calculate) == "no": 
        calculate = int(0)
    else:
        while str(calculate) != "yes" and str(calculate) != "no":
            calculate = raw_input("\nYou want to continue (yes/no): ")
        if str(calculate) == "yes":
            calculate = int(1)
        elif str(calculate) == "no": 
            calculate = int(0)