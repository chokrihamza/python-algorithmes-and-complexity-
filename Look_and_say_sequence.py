def next_number(sequence):
    result=[]
    i=0
    while i<len(sequence):
        count=1
        while i+1<len(sequence) and sequence[i]==sequence[i+1]:
            i += 1
            count+=1
        result.append(str(count)+sequence[i])
        i+=1
    return "".join(result)
n=20
s="1"
for i in range(n-1):
    s=next_number(s)

print(s)