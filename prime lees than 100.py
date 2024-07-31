def prime(n):
    l=[]
    for i in range(1,n+1):
       for j in range(2,i):
           if(i%j==0):
              break
       else:
            l.append(i)
    return l

max=int(input("Enter the max limit:"))
a=prime(max)
print("The prime numbers<%d are -"%max,*a,sep=" ")