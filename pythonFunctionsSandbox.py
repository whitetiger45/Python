# your code goes here
 
x = "hello there"
 
def f(p1,p2):
    return p1 + p2
 
def g(p):
    return (p, x, [1, "two", 3, [4,"five"]])
 
print str(f(9, 9))
 
y = g(9)
 
for x in y:
    print x 
 
for x in y[2]:
    print x
 
for x in range(len(y[2]) + 1):
    print x
 
i = 0
if (len(y[2][3]) > 0):
    for x in y[2][3]:
        i += 1;
        print str(i) + ": " + str(x)