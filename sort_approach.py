# bubble sort
# complexity O(n^2)
input_array=[1,5,7,8,10,2,5,14,20,7,80,50,51]
def bubble_sort(input_array):

    for i in range(len(input_array)-1):
        for j in range(0,len(input_array)-i-1):
            if input_array[j]>=input_array[j+1]:
                input_array[j],input_array[j+1]=input_array[j+1],input_array[j]
    return input_array

print(bubble_sort(input_array))

# insertion sort
# like the card playing
# complexity O(n^2)

def insertion_sort(input_array):
    for i in range(1,len(input_array)):
        key=input_array[i]
        j=i-1
        while j>0 and key< input_array[j]:
            input_array[j+1]=input_array[j]
            j-=1

        input_array[j + 1]=key
    return input_array
print(insertion_sort(input_array))