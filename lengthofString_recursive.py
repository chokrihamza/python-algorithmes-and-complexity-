# develop the len fucntion without using
# len() in python

input_str="hamza chokri"
#print(len(input_str))

# develop it itirative
def len_itirative(input_str):
    count=0
    for i in range(len(input_str)):
        count+=1
    return count

# len using recursion algorithme

def len_recusive(input_str):
    # base condition :
    if input_str=="":
        return 0
    return 1+len_recusive(input_str[1:])


print(len_itirative(input_str))
print(len_recusive(input_str))
