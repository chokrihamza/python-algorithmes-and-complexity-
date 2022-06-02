# find the bitonic sequence
# example
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 1
# 1 6 5 4 3 2 1

# wirte an algorithme to find a bitoic sequence
A=[1,2, 3 ,4 ,5, 4, 3, 2, 1]
B=[1, 2 ,3 ,4, 1]
C=[1, 6, 5, 4 ,3, 2, 1]

# first find the highest point
# find the peak element using binary search 
def find_peak_number(data):
    low=0
    high=len(data)-1

    while low<high:
        mid=(low+high)//2
        if data[mid]<data[mid+1]:
            low=mid+1
        elif data[mid-1]>data[mid]:
            high=mid-1
        else:
            return data[mid]
    return None
            

print(find_peak_number(A))
print(find_peak_number(B))
print(find_peak_number(C))