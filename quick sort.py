def quick_sort(l,lb,ub):
    if(lb<ub):
        i=partition_list(l,lb,ub)
        quick_sort(l,lb,i-1)
        quick_sort(l,i+1,ub)
        
def partition_list(l,lb,ub):
    key=l[lb]
    start=lb+1
    end=ub
    while(start<end):
        while(start<=end and l[start]<key):
            start=start+1
        while(start<= end and l[end]>key):
            end=end-1
        if(start<end):
              (l[start],l[end])=(l[end],l[start])
        else:  
              (l[lb],l[end])=(l[end],l[lb])
    return end



l=[]
n=int(input("Enter the number of elements of the list:"))
print("Enter the list elements:")
for i in range(0,n):
    ele=int(input())
    l.append(ele)
quick_sort(l,0,n-1)
print("After sorting the list is:- ")
print(l)