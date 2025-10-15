import math
def toBinary(n):
    return bin(n)[2:]

print(toBinary(20))
    
def divide(n, m):
    o = 0
    while n >= m:
        n -= m
        o += 1
    return o

print(divide(100,2))

def reverse(n):
    n = str(n)
    a = []
    for c in n:
        a.append(c)
    a.reverse()
    o = ""
    for c in a:
        o = o + c
    return o
    
print(reverse(1234))


def zerosInFactorial(n):
    f = str(math.factorial(n))
    c = 0
    for d in f:
        if d == "0":
            c += 1
    return c
    
print(zerosInFactorial(10))
