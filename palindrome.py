# read a string back and forward
s="was it a cat i saww?"

# clean our data
s=''.join([i for i in s if i.isalpha()]).replace(" ","").lower()
print(s)

def is_palindrome(s):
    s=''.join([i for i in s if i.isalpha()]).replace(" ","").lower()
    if s==s[::-1]:
        return True
    return False

print(is_palindrome(s))

# the recursive solution of palindrome
def recursive_palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        while not s[i].isalnum() and i<j:
            i+=1
        while not s[i].isalnum() and i<j:
            j-=1
        if s[i].lower()!=s[j].lower():
            return False
        i+=1
        j-=1

    return True


print(recursive_palindrome(s))
