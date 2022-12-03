# program to approximate the integral of a function using Simpson's method

h = 0.1 

def f(x):
    return 16/(16+x**2)

def simpson(a, b):
    return (h/3)*(f(a)+f(b)+4*sum([f(a+(2*j-1)*h) for j in range(1, int((b-a)/h))])+2*sum([f(a+2*j*h) for j in range(1, int((b-a)/(2*h)))]))

print(simpson(0, 4))