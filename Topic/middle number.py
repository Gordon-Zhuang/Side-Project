<<<<<<< HEAD
def middlenum(a,b,c):
    if b > a:
        a,b = b,a
    if c > a:
        return a
    if c > b:
        return c
    return b
=======
def middlenum(a,b,c):
    if b > a:
        a,b = b,a
    if c > a:
        return a
    if c > b:
        return c
    return b
>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
print(middlenum(3,1,2))