# your code goes here
import timeit

vals = {}
vals2 = {}
vals3 = {}
def nested(d):
    for k,v in d.items():
        # print(k,v)
        for nk,nv in v.items():
            # print(nk,nv)
            vals2.update({nk : nv})
def reglr(d):
    for k,v in d.items():
        # print(k,v)
        vals3.update({k : v})

def comprPrint(**kwargs):
    # for x in kwargs:
        # print( x, kwargs[x])
    # [ [print (kwargs[x][k]) for k in kwargs[x]] for x in kwargs ]
    # [ [print (k,kwargs[x][k]) for k,v in kwargs[x].items()] for x in kwargs ]
    [ [vals.update({k:kwargs[x][k]}) for k,v in kwargs[x].items()] for x in kwargs ]
    
def compr(**kwargs):
    # for x in kwargs:
        # print( x, kwargs[x])
    # [ [print (kwargs[x][k]) for k in kwargs[x]] for x in kwargs ]
    # [ [print (k,kwargs[x][k]) for k,v in kwargs[x].items()] for x in kwargs ]
    [ [vals.update({k:kwargs[x][k]}) for k,v in kwargs[x].items()] for x in kwargs ]

items_dict = {"x":{"a":1,"b":2,"c":3}, "y" : {"d":4,"e":5,"f":6}, "z" :{"g":7,"h":8,"i":9}}
# test(a='1',b='2',c='3')
# compr(**items_dict)
# result = compr(**items_dict)
# nested(items_dict)
# [ reglr(v) for k,v in items_dict.items() ]
# print (vals)

t1 = (timeit.timeit('comprPrint(**items_dict)', number=1,globals=globals()))
# t1 = (timeit.timeit('[ [print (k,items_dict[x][k]) for k,v in items_dict[x].items()] for x in items_dict ]', number=1,globals=globals()))
t2 = (timeit.timeit('nested(items_dict)', number=1,globals=globals()))
t3 = (timeit.timeit('[ reglr(v) for k,v in items_dict.items() ]', number=1,globals=globals()))
_names = {'t1':t1,'t2':t2,'t3':t3}
_comp = max(t1,t2,t3)
_winner = [k for k,v in _names.items() if str(v) in str(_comp) ]
print("{0}: {1} wins!".format(_winner, _names.get(_winner[0])))

[ print("{0}: {1}".format(k,v)) for k,v in _names.items() ]
