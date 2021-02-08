# Errado

def approx_derivative(f, x, delta = 10 ** -6):
    return (f(x+delta) - f(x-delta)) / 2 * delta



def approx_derivative_2(x):
    return approx_derivative(x)

#def approx_integral(f, lo, hi, num_regions):