data=[2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target=28

# Linear Search
def Linear_Search(data,target):
    # linear time solution not so good
    # so we can optimize it O(n)
    for i in range(len(data)):
        if data[i]==target:
            return True

    return False

# itirative binary search
# the set must be in order !!!!
# O(log(n))
def binary_search_itirative(data,target):
    low=0
    high=len(data)-1
    while low<high:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
# recursive version of binary search

def binary_search_recurive(data,target,low,high):
    if low>high:
        return False
    else:
        mid= (low+high)//2
        if target==data[mid]:
            return True
        if target<data[mid]:
            return binary_search_recurive(data,target,low,mid-1)
        if target>data[mid]:
            return binary_search_recurive(data,target,mid+1,high)



print(binary_search_itirative(data,target))
print(binary_search_recurive(data,target,0,len(data)-1))