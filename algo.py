

A=[20,30,14,50,52,78,90,20,14,50,65,45,78]

# selelction sorrt algorithme
# complextiy in O(n^2)
# space O(1)

def selelction_sort(array):
    for i in range(len(array)):
        min_array=i
        for j in range(i+1,len(array)):

            if array[min_array]>array[j]:
                min_array=j
        # swap that elements
        array[i],array[min_array]=array[min_array],array[i]

    return array

#print(selelction_sort(A))

# insertion sort algorithme
# complextiy in O(n^2)
# space O(1)

def insertion_sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return array
print(insertion_sort(A))