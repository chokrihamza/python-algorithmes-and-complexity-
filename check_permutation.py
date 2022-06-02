is_permutation_1="good"
is_permutation_2="ood"

# first approach
#
# time complexity is O(nlogn) due to the sort method
# space O(1) cause we just ckeck
def is_perm_1(str_1,str_2):
    # pre treatment
    # normalizing
    str_1=str_1.lower()
    str_2 = str_2.lower()
    if len(str_1)!=len(str_2):
        return False
    # use built in sorted function nlogn
    str_1="".join(sorted(str_1))
    str_2 ="".join(sorted(str_2))
    n=len(str_1) # the same len for both
    for i in range(n):
        if str_1[i]!=str_2[i]:
            return False
        return True

#print(is_perm_1(is_permutation_1,is_permutation_2))


# time complexity is O(n)
# space O(n) cause we use hash table


# second method
def is_perm_2(str_1,str_2):
    # using the hash table
    # pre treatment
    # normalizing
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    if len(str_1)!=len(str_2):

        return False
    perm_dict=dict()
    for i in str_1:
        if i in perm_dict:
            perm_dict[i]-=1

        else:
            perm_dict[i]=1

    for i in str_2:
        if i in perm_dict :
            perm_dict[i] -= 1

        else:
            perm_dict[i] = 1

    for i in perm_dict.values():
        if i%2==0 or i==0:
            return True



print(is_perm_2(is_permutation_1,is_permutation_2))