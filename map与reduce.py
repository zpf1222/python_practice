def f(x):
    return x*x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9] )
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


from functools import reduce
def add(x,y):
    return x+y
a = reduce(add,[1,3,5,7,9])
print(a)

#把序列[1, 3, 5, 7, 9]变换成整数13579
from functools import reduce
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

print("_________________________________________")

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))