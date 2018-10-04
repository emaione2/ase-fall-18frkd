# ase_lab
# implement calculator.py with 2 functions sum and divide and must work with z numbers
# python does not use interfaces, it has modules

def sum(m, n):
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1
    return result

def divide(m, n):
    result = 0
    sign = 1
    if n == 0:
        raise ZeroDivisionError("You cannot divide by 0!")
    if (n < 0 and m > 0) or (n > 0 and m <0):
        sign = -1
    n = abs(n)
    m = abs(m)
    while m-n >= 0:
        m -= n
        result += 1
    return sign * result

def subtract(m,n):
    res = m
    if n > 0:
        for i in range(0, n):
            res -= 1
    else:
        for i in range(0, -n):
            res += 1

    return res

def multiply(m,n):
    if(m==0 or n==0):
        return 0

    res = 0
    sign = 1
    if (m < 0):
        m = abs(m)
        sign = sign * (-1)
    if (n < 0):
        n = abs(n)
        sign = sign * (-1)
    for i in range(n):
        res+=m
    return res * sign