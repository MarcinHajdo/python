 from random import randint
X = [randint(0, 100) for x in range(1000)]
def sort(x):
    if(len(x)<2):
        return x
    result=[]   
    d=int(len(x)/2)
    a=sort(x[:d])
    b=sort(x[d:])
    while (len(a)>0) and (len(b)>0):
        if a[0]<b[0]:
            result.append(a[0])
            a.pop(0)
        else:
            result.append(b[0])
            b.pop(0)
       
    result += a
    result += b
    return result   
print(sort(X))   
