A=[1,2,3,4,5,5,6,7,8,9,1,0,10,10]
target=1

# just go through all the array
def find_duplicated_target(data,target):
    i=0
    t=None
    while i < len(data):
        if data[i]==target:
            t=data[i]
            break

        i+=1

    k=0
    while k < len(data):
        if t==data[k] and k!=i:
            
            return "Duplicated "

        k+=1
    return "Not Duplicated"


print(find_duplicated_target(A,5))