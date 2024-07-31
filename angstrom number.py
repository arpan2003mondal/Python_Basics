#angstrom number

def power(num):
    count=0
    while(num!=0):
        rem=num%10
        num=num//10
        count=count+1
    return count

def angstrom(num,pow):
    sum=0
    while(num!=0):
        rem=num%10
        num=num//10
        a=(rem**pow)
        sum=sum+a
    return sum
    
num=int(input("Enter your number:"))
pow=power(num)
ang=angstrom(num,pow)
if(num==ang):
    print("%d is an Angstrom Number"%num)
else:
      print("%d is not an Angstrom Number"%num)