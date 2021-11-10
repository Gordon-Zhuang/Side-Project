
def middlenum(a,b,c):
    if b > a:
        a,b = b,a
    if c > a:
        return a
    if c > b:
        return c
    return b

def middlenum(a,b,c):
    if b > a:
        a,b = b,a
    if c > a:
        return a
    if c > b:
        return c
    return b

print(middlenum(3,1,2))