x=2
y=3
# solution
# do 3+3 two times
#print(x*y)

def product_recursive(x,y):
    if x<y:
        return product_recursive(y,x)
    if y==0:
        return 0
    return x+product_recursive(x,y-1)
s
print(product_recursive(2555,50))