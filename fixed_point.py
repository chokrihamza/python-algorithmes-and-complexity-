A=[1,2,1,3,5,5,5,6,6,6,10]
# time complexity O(n)
# space complexity O(1)
def linear_fixed_point(data):

    for i in range(len(data)):
        if data[i]==i:
            print(A[i])
    return None


print(linear_fixed_point(A))

# using binary search
# the elements must be soted and distinct
#    0  1 2 3 4
B=[-10,-5,0,3,7]

def find_fixed_point(data):
    low=0
    high=len(data)-1
    while low<high:
        mid=(low+high)//2
        if data[mid]<mid:
            low=mid+1
        elif data[mid]>mid:
            high=mid-1
        else:
            return A[mid]
    return None

print(find_fixed_point(B))