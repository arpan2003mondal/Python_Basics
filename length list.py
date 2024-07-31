#python program to count the number of elements in a list
def length(l):
    if(l==[]):
        return 0
    else:
        return 1+length(l[1: ])


l=[]
n=int(input("Enter the number of elements of the list:"))
print("Enter the list elements:")
for i in range(0,n):
    ele=int(input())
    l.append(ele)
len=length(l)
print('The number of elements in the list is-',len)
