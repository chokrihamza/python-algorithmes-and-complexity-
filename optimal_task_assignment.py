# optimal task assignment
# using Greed approach
# as enter we have an array
# second sort that array aka tasks
# pick the longest and the shortest means the first and the last element in the table
# complexity O(nlogn)
A=[6,3,2,7,5,5,1]
A=sorted(A)

for i in range(len(A)//2):
    print(A[i],A[~i])
