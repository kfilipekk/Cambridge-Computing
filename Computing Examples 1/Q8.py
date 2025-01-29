import numpy as np
N_values = [10**2, 10**5, 10**6, 10**8]
a,b = 1,1

#Volume/area
#Calculates the mean of the function
def monte_carlo(function, a, b, N):
    x_random = np.random.uniform(-a, a, N)
    y_random = np.random.uniform(-b, b, N)
    function_values = function(x_random, y_random)
    return 4*a*b * np.mean(function_values)

#Part a
def f1(x, y): return np.exp(x*y) * np.cos(y)**2 * np.sin(x**2)
for N in N_values:
    result = monte_carlo(f1, a, b, N)
    print(f"Approximate integral for N={N}: {result}")

#Part b
def f_circle(x, y): return np.where(x**2 + y**2 <= 1, 1, 0)
for N in N_values:
    result = monte_carlo(f_circle, a, b, N)
    print(f"Approximate integral for N={N}: {result}")
    print(f"Error: {abs(result - np.pi)}")
#This is for a cylinder.
#Try as half sphere 