def f(x):
    return x ** 2

def g(x):
    return x * 2

def composite_result(f, g, x):
    return f(g(x))

def composite(f, g):
    fog = lambda x : f(g(x))
    return fog
