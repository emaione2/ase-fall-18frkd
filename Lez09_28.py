def sum(m,n):
    res = m
    if n<0:
        for i in range(0, -n):
            res -= 1
    else:
        for i in range(0,n):
            res+=1

    return res

a=21
b=-3
print("sum->",a,"+",b,"=",sum(a,b))

def divide(m,n):
    res=0
    sign=1
    if(m<0):
        m = abs(m)
        sign = sign * (-1)
    if (n < 0):
        n=abs(n)
        sign = sign * (-1)
    while(m>=0):
        m=m-n
        if(m>=0):
            res+=1
    return res*sign

a=-21
b=3
print("divide->",a,":",b,"=",divide(a,b))

class calculator:
    def __init__(self):
