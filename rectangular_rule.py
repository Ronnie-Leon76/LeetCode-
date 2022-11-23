from sympy import integrate, Symbol

h = 0.1
X_k = [0,]
f_X_k = []


# function to find the exact solution
def integrate_(f, x, a, b):
    return integrate(f, (x, a, b))

x = Symbol('x', real=True)
f = 3 * x ** 2 + 6

exact = integrate_(f, x, 0, 2)


for i in range(1, 21):
    X_k.append(X_k[i-1] + h)
    

for i in X_k:
    val = 0
    val = 3*i**2 + 6
    f_X_k.append(val)
    
def lower_rectangular_rule():
    sum = 0
    for i in range(0, 20):
        sum += f_X_k[i]
    return sum*h

def upper_rectangular_rule():
    sum = 0
    for i in range(1, 21):
        sum += f_X_k[i]
    return sum*h


if __name__ == "__main__":
    print("Lower Rectangular Rule Value: ", lower_rectangular_rule())
    print("Upper Rectangular Rule Value: ", upper_rectangular_rule())
    print("Exact: ", exact)
    print("Errors: %f, %f" % (abs(lower_rectangular_rule() - exact), abs(upper_rectangular_rule() - exact)))
    
    
