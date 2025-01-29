import math

def integrate(f, a, b, x, w):
    integral = sum(f(x_point)*weight for x_point, weight in zip(x, w))#Calculates the function at a sample point and multiplies it by the weight
    return (b-a) * integral

a, b = 0, 10 #Limits of integral
exact_solution = 8500 / 3  
def f(x): return x**3 + x**2 

#Trapezium Rule
x = (a, b)
w = (0.5, 0.5)
integral = integrate(f, a, b, x, w)
print(f"Integral: {integral}")
print(f"Error: {abs(integral - exact_solution)}")

#Simpson's rule
x = (a, (a + b) / 2, b)
w = (1/6, 2/3, 1/6)
integral = integrate(f, a, b, x, w)
print(f"Integral:", integral)
print(f"Error: {abs(integral - exact_solution)}")

#Gauss quadrature
x = ((a + b) / 2 - (b - a) / (2 * math.sqrt(3)),
     (a + b) / 2 + (b - a) / (2 * math.sqrt(3)))
w = (0.5, 0.5)
integral = integrate(f, a, b, x, w)
print(f"Integral: {integral}")
print(f"Error: {abs(integral - exact_solution)}")

#For a more complex function divide into smaller subintervals
