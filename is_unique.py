unqiue_str="abcdefg      "
not_unique_str="aabbccDD"

def nomralize_input(input_str):
    input_str=input_str.replace(" ","")
    return input_str.lower()

def is_unique_1(input_str):
    input_str=nomralize_input(input_str)
    d=dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i]=1
    return True
def is_unique_2(input_str):
    if len(set(input_str))==len(input_str):
        return True
    return False





print(is_unique(unqiue_str))