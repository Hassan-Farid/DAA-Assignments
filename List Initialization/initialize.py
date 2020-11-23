def ListConcat():
    l = []
    for i in range(1000):
        l = l + [i]

def ListAppend():
    l = []
    for i in range(1000):
        l.append(i)

def ListComp():
    l = [i for i in range(1000)]

def ListRange():
    l = list(range(1000))

from timeit import Timer, timeit

t1 = Timer("ListConcat()", "from __main__ import ListConcat")
print("concat ",t1.timeit(number=1000), "milliseconds")

t2 = Timer("ListAppend()", "from __main__ import ListAppend")
print("append ",t2.timeit(number=1000), "milliseconds")

t3 = Timer("ListComp()", "from __main__ import ListComp")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = Timer("ListRange()", "from __main__ import ListRange")
print("list range ",t4.timeit(number=1000), "milliseconds")