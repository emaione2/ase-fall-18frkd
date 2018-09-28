# ase_lab
# implement calculator.py with 2 functions sum and divide and must work with z numbers
# python does not use interfaces, it has modules

def sum(m, n):
    result = m
    if n < 0:
        for i in range(-n):
            result -= 1
    else:
        for i in range(n):
            result += 1
    return result

def divide(m, n):
    if n > m:
        return 0
    res = 0
    if n < 0:
        while(m >= 0):
            m -= -n
            res -= 1
        res += 1
    else:
        while(m >= 0):
            m -= n
            res += 1
        res -= 1
    return res

def divideLab(m, n):
    result = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0

    return result