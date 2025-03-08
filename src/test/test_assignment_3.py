import numpy as np

def euler_method(f, t0, y0, h, n):
    t_values = np.zeros(n+1)
    y_values = np.zeros(n+1)
    
    t_values[0] = t0
    y_values[0] = y0
    
    for i in range(n):
        t_values[i+1] = t_values[i] + h
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    return y_values

def runge_kutta_method(f, t0, y0, h, n):
    t_values = np.zeros(n+1)
    y_values = np.zeros(n+1)
    
    t_values[0] = t0
    y_values[0] = y0
    
    for i in range(n):
        t = t_values[i]
        y = y_values[i]
        
        k1 = f(t, y)
        k2 = f(t + h/2, y + h*k1/2)
        k3 = f(t + h/2, y + h*k2/2)
        k4 = f(t + h, y + h*k3)
        
        t_values[i+1] = t + h
        y_values[i+1] = y + h * (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return y_values

# Define the function t - y^2
def f(t, y):
    return t - y**2

def main():
    # Parameters for the functions
    t0 = 0
    y0 = 1
    t_end = 2
    n = 10
    h = (t_end - t0) / n
    
    # Question 1
    y_euler = euler_method(f, t0, y0, h, n)
    
    # Question 2
    y_rk = runge_kutta_method(f, t0, y0, h, n)
    
    # Final values
    print(f"{y_euler[-1]}")
    print(f"{y_rk[-1]}")

if __name__ == "__main__":
    main()