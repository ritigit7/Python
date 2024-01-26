# type ipython
# print(hash("dlksjf"))

def f(x):
    for i in range(0,x):
        return i**2
def g(x):
    return x**4
def h(x):
    return x**8

import timeit
print(timeit.timeit('[func(1) for func in (f,g,h)]', globals=globals()))