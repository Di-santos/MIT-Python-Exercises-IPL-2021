def f(x):
    return x ** 2

def approx_derivative(f, x, delta = 10 ** -6):
    return (f(x+delta) - f(x-delta)) / (2 * delta)

def approx_derivative_2(f, delta = 10 ** -6):
    aprox = lambda x : (f(x+delta) - f(x-delta)) / (2 * delta)
    return aprox
    
def approx_integral(f, lo, hi, regioes):
    altura = float(hi - lo) / regioes
    soma = 0.5 * (f(lo) + f(hi))

    for intervalo in range(1, regioes):
        soma += f(lo + intervalo * altura)
    
    return soma * altura
