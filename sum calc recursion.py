def sumfunc(n,sum):
    if(n==0):
        return sum
    else:
        sum=sum+n
        n=n-1
        return sumfunc(n,sum)
        
n=int(int(input('Enter the last term: ')))
print("The sum is--",sumfunc(n,0))

