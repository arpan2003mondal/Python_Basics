def merge_sort(l,lb,ub):
    if(lb<ub):
        mid=(lb+ub)//2
        merge_sort(l,lb,mid)
        merge_sort(l,mid+1,ub)
        merge(l,lb,mid+1,mid,ub)

def merge(l,lb1,lb2,ub1,ub2):
    a=[]
    i=lb1
    k=0
    while(lb1<=ub1 and lb2<=ub2):
        if(l[lb1]<l[lb2]):
            a.append(l[lb1])
            lb1=lb1+1
        else:
            a.append(l[lb2])
            lb2=lb2+1
    while(lb1<=ub1):
            a.append(l[lb1])
            lb1=lb1+1
    while(lb2<=ub2):
            a.append(l[lb2])
            lb2=lb2+1
    for p in range(i,ub2+1):
            l[p]=a[k]
            k=k+1


l=[]
n=int(input("Enter the number of elements of the list:"))
print("Enter the list elements:")
for i in range(0,n):
    ele=int(input())
    l.append(ele)
merge_sort(l,0,n-1)
print("After sorting the list is:- ")
print(l)