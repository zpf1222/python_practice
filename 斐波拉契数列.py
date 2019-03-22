def fib(max):  # max 为循环的次数
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a , b = b , a + b
        n = n + 1
    return "done"

fib(15)


