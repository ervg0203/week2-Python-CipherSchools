def greater(a,b):
    if a > b:
        return a
    return b

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

def new_greatest(a,b,c):
    # bigger = greater(a,b)
    return greater(greater(a,b), c) 

print(greatest(100,40,30))