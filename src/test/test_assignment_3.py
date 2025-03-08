import numpy as np

def euler_method(f, t0, y0, h, n):
    t_values = np.zeros(n+1)
    y_values = np.zeros(n+1)
    
    t_values[0] = t0
    y_values[0] = y0
    
    for i in range(n):
        t_values[i+1] = t_values[i] + h
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    return t_values, y_values

# Define the function t - y^2
def f(t, y):
    return t - y**2

def main():
    # Question 1
    t0 = 0
    y0 = 1
    t_end = 2
    n = 10
    h = (t_end - t0) / n
    
    # Solve using Euler method
    t_euler, y_euler = euler_method(f, t0, y0, h, n)
    
    
    # Print the final values
    print(f"{y_euler[-1]}")

if __name__ == "__main__":
    main()