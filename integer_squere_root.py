k=300

# exemple
# if k=12
# 1^2=1
# 2^2=4
# 3^2=9
# 4^2=16
# complexity of O(k)
# so we want to optimize the solution using binary search




def integer_square_root(k):
    low=0
    high=k
    while low <= high:
        mid=(low+high)//2
        mid_squared=mid*mid
        if mid_squared <=k:
            low=mid+1
        else:
            high=mid-1

    return low-1

print(integer_square_root(k))