def square(x):
    return x**2 

def fourth_power(x):
    return square(square(x))

def perfect_square(x):
    if str(x ** 0.5).endswith('.0') or x == 0 or x == 1:
        return True
    
    else:
        return False
