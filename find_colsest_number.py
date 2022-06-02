# find the closest number of an integer in an array
# the array must be sorted
A=[1,2,4,5,6,6,8,9,10,11,12]
#A=[2,5,6,7,8,8,9]

def closest_number(data,target):
    min_diff=float("inf")
    low=0
    high=len(data)-1
    closest_num=None

    # breaf check
    if len(A)==0:
        return None
    if len(A)==1:
        return A[0]
    while low < high :
        mid=(low+high)//2
        if mid+1<len(A):
            min_diff_right=abs(data[mid+1]-target)
        if mid > 0:
            min_diff_left=abs(data[mid-1]-target)
        if min_diff_left<min_diff:
            min_diff=min_diff_left
            closest_num=data[mid-1]
        if min_diff_right<min_diff:
            min_diff=min_diff_right
            closest_num = data[mid + 1]

        # move mid point
        if data[mid]<target:
            low=mid+1
        elif data[mid]>target:
            high=mid-1
        else:
            return data[mid]

    return closest_num








print(closest_number(A,12))


# linear search

def linear_closest_number(data,target):
    diff=float("inf")
    closest=0
    i=0
    while i<len(data):
        if abs(data[i] - target) < diff:
          diff=abs(data[i]-target)
          closest=data[i]

        i+=1
    return closest

#print(linear_closest_number(A,12))


