#python program to compute reverse of a number
def reverse_num(n):
    l=[]
    
    while(n!=0):
        r=n%10
        n=n//10
        l.append(r)
    return l
    
num=int(input("Enter your number: "))
a=[]
a=reverse_num(num)
print("Reverse of %d is - "%num,*a,sep="")
#print(*a,sep="")

