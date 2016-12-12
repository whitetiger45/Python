#!/usr/bin/python
calculate = 1
while calculate :
    ops = ['1) +', '2) -', '3) *', '4) /', '5) **', '6) //', '7) dec-to-hex converter', '8) hex-to-dec converter', '9) Exit']
    print "\nWhat would you like to do:\n_______________________\n"
    for c in ops:
        print str(c)

    op = raw_input("\nEnter an operand: ")
#-------------------------------------------------------------------------
    if int(op) >= 1 and int(op) < 8:
        x = raw_input("\nEnter x: ")
        y = raw_input("\nEnter y: ")
    elif int(op) == 9:
        calculate = "no"
#-------------------------------------------------------------------------
    if op == "+" or int(op) == 1: 
        userSelection = 1
        calc = float(x) + float(y)
        if int(op) == 1:
            op = "+"
    elif op == "-" or int(op) == 2:
        userSelection = 2
        calc = int(x) - int(y)
        if int(op) == 2:
            op = "-"
    elif op == "*" or int(op) == 3: 
        userSelection = 3
        calc = int(x) * int(y)
        if int(op) == 3:
            op = "*"
    elif op == "/" or int(op) == 4:
        userSelection = 4
        if int(y) == 0:
            print "Cannot divide by 0\n"
        else:
            calc = int(x) / int(y)
        if int(op) == 4:
            op = "/"
    elif op == "**" or int(op) == 5:
        userSelection = 5
        calc = int(x) ** int(y)
        if int(op) == 5:
            op = "**"
    elif op == "//" or int(op) == 6:
        if int(y) == 0:
            print "Cannot divide by 0\n"
        else:
            calc = int(x) // int(y)
        userSelection = 6
        if int(op) == 6:
            op = "+"
    elif int(op) == 7:
        userSelection = 7
        x = raw_input("\nEnter decimal number: ")
        calc = hex(int(x))
    elif int(op) == 8:
        userSelection = 8
        x = raw_input("\nEnter hexidecimal number: ")
        calc = int(x, 16)

#-------------------------------------------------------------------------
    if userSelection >= 1 and userSelection < 7:
        if float(y) != 0:
            print "\n" + str(x) + " " + str(op)  + " " + str(y) + ": " + str(calc)
    elif userSelection == 7 or userSelection == 8:
        print  "\nDecimal Value: " + str(x) + ", Hexidecimal Value: " + str(calc)
    
    if userSelection != 9:
        calculate = raw_input("\nDo you want to make another calculation? (yes/no): ")

    if str(calculate) == "yes" or str(calculate) == "y":
        calculate = int(1)
    elif str(calculate) == "no" or str(calculate) == "n": 
        calculate = int(0)
    else:
        while str(calculate) != "yes" and str(calculate) != "no":
            calculate = raw_input("\nDo you want to make another calculation? (yes/no): ")
        if str(calculate) == "yes":
            calculate = int(1)
        elif str(calculate) == "no": 
            calculate = int(0)
