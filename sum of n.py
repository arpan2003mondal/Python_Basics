def sum_func(t):
    sum=0
    l=[]
    for i in range(1,t+1):
        sum=sum+i
        l.append(sum)
    print(*l,sep="+")
    lsum=0
    for j in range(len(l)-1,-1,-1):
        lsum=lsum+l[j]
        
    print("The sum is -",lsum)
        
        
t=int(input('Enter the upto term-'))
sum_func(t)