def tri(maxiteration):
    n=1
    a=[]
    b=[1]
    while n<maxiteration+1:
        n=n+1
        a.clear()
        for iteam in b:
            a.append(iteam)
        yield a
        b.clear()
        for i in range(0,n):
            if i==0 or i==n-1:
                b.append(1)
            else:
                b.append(a[i-1]+a[i])
    return 'DONE!'
for i in tri(10):
    print(i)


def triangle(n):
    l, index = [1], 0
    while index < n:
        print(l)
        l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
        index+=1

triangle(10)