#python program to find the sum of integers
def sum_int(l,sum):
    if l==[]:
        return sum
    else:
        if(isinstance(l[0],int)):
            sum=sum+l[0]
            return sum_int(l[1:],sum)
        else:
            return sum_int(l[1: ],sum)

l=[2,3,1.2,5,2.2,3.1,6,5]
'''l=[]
n=int(input("Enter the number of elements of the list:"))
print("Enter the list elements:")
for i in range(0,n):
    ele=float(input())
    l.append(ele)
print(l)'''
print("The sum of integers in the list is-",sum_int(l,0))