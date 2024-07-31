def sum_rec(n,sum,term):
    if(term==n+1):
        return sum
    else:
        sum=sum+term
        term=term+1
        return sum_rec(n,sum,term) 

n=int(input('Enter the max term:-'))
print("Final sum is-",sum_rec(n,0,1))