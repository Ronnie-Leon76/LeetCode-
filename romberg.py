"""
Author: Ronnie Leon
Date: 2022-3-12
Description: This program uses the Romberg method to approximate the integral of a function.

"""

def f(x):
    return 16/(16+x**2)

def romberg(a, b, iterations):
    R = [[0 for i in range(iterations)] for j in range(iterations)]
    for i in range(0, iterations):
        h = (b-a)/(2**i)
        n = int((b-a)/h)
        if n == 1:
            R[i][0] = (h/2)*(f(a)+f(b))
        else:
            R[i][0] = (h/2)*(f(a)+f(b)) + sum([f(a+(2*j-1)*h) for j in range(1, n)])
    print(R)
    for j in range(1, iterations):        
        for i in range(j,iterations):
                R[j][i] = (4**i*R[j-1][i]-R[j-1][i-1])/(4**i-1)
    print(R)
    return R[iterations-1][iterations-1]

print(romberg(0, 4, 5))
