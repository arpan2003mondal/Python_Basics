
def fibo(n=2000):
    s=[1]
    p=0
    q=1
    r=0
    for i in range(n):
        r=p+q
        if (r>n):
            break
        s.append(r)
        p=q
        q=r
    return s
def prime(a):
    i=0
    c=[]
    for i in range(2,len(a)):
        for j in range(2,a[i]):
            p=j
            if (a[i]%j)==0:
                break
        else:
            c.append(a[i])
    return c
a=fibo()
b=prime(a)
print(b)
