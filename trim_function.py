input_str="     chok ri     l  "

#print(input_str.strip(),"how are you ")

def strip_str(input_str):
    strip_one=""
    for i in range(len(input_str)-1):
        if input_str[i]!=" ":
            strip_one=strip_one+input_str[i]
    return strip_one

print(strip_str(input_str)+" how are you")

def delete_white_space(input_str):
    pass