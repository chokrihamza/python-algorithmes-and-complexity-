# find uppercase in a string itirative and recursivly
input_str_1="chokriHamza"
input_str_2="ChokriHamza"
input_str_3="chokrihamza"

def find_uppercase_itirative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase caracter found"

def find_uppercase_recursive(input_str,index=0):
    if input_str[index].isupper():
        return input_str[index]
    if index==len(input_str)-1:
        return "No uppercase element found"
    return find_uppercase_recursive(input_str,index+1 )




print(find_uppercase_itirative(input_str_1))
print(find_uppercase_itirative(input_str_2))
print(find_uppercase_itirative(input_str_3))
print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))