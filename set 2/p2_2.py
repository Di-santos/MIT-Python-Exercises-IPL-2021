def prime(num):

    if num == 0 or num == 1:
        return False

    elif num == 2:
        return True

    elif num % 2 == 0:
            return False
        
    else:
        for i in range(3, round(num/2), 2):
            if num % i == 0:
                return False

    return True
