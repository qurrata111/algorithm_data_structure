def max2 (a, b):
    max = a if a >= b else b
    return max

def max3 (a, b, c):
    return max2(a, max2(b, c))

def max9 (a, b, c, d, e, f, g, h, i):
    return max3(max3(a, b, c), max3(d, e, f), max3(g, h, i))

print(max2(9, 0))
print(max3(5, 100, -9))
print(max9(1,2,3,4,5,64,38,19,10))