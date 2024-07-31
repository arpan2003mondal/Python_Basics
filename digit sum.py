#python program to find sum of a number of its digits
num=int(input("Enter your number-"))
sum=0
n=num
while(num!=0):
    rem=num%10
    num=num//10
    sum=sum+rem
print(" %d digit sum is:-"%n,sum)