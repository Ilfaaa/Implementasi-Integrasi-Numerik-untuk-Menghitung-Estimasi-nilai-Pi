import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def trapezoidal_rule(a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    integral = h * (0.5*y[0] + 0.5*y[N] + sum(y[1:N]))
    return integral

def calculate_pi(N):
    a = 0
    b = 1
    pi_approx = trapezoidal_rule(a, b, N)
    return pi_approx

def test():
    N_values = [10, 100, 1000, 10000]
    reference_pi = 3.14159265358979323846
    for N in N_values:
        start_time = time.time()
        pi_approx = calculate_pi(N)
        end_time = time.time()
        error = np.abs(pi_approx - reference_pi)
        print(f"N = {N}, Approximated Pi = {pi_approx}, Error = {error}, Execution Time = {end_time - start_time} seconds")

test()
